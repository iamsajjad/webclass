from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def accountsPage(request):

    # get next page
    nextPage = request.GET.get('next', '/')

    if User.objects.filter(username=request.user).exists():
        return HttpResponseRedirect('/')
    else:
        return render(request, 'author/author.html', {'nextPage': nextPage})

def signIn(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    author = str(username)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(request.POST.get('next', '/'))
    else:
        return HttpResponseRedirect('/account/')

def signUp(request):

    original = 'admin'
    code = request.POST.get('code', '')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    if str(code) == original:
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        except:
            return HttpResponseRedirect('/account/')
        else:
            return signIn(request)
    else:
        return HttpResponseRedirect('/account/')

def signOut(request):

    logout(request)

    return render(request, 'author/author.html')
