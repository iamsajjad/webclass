from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

@login_required(login_url='/account/')
def classesPage(request):

    response = {

    }
    return render(request, 'classesPage.html', response)

def aboutPage(request):
    return render(request, 'aboutPage.html')

def contactPage(request):
    return render(request, 'contactPage.html')

def servicesPage(request):
    return render(request, 'servicesPage.html')

