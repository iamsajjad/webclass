from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from classes.models import *

# Create your views here.

@login_required(login_url='/account/')
def classesPage(request):

    classes = Classes.objects.all()
    response = {
        'classes' : classes,
    }

    return render(request, 'classesPage.html', response)

@login_required(login_url='/account/')
def createClassPage(request):
    return render(request, 'createClassPage.html')

@login_required(login_url='/account/')
def classPage(request, classPrimary):

    requstedClass = Classes.objects.get(primary=classPrimary)
    posts = requstedClass.posts.all().reverse()

    response = {
        'requstedClass' : requstedClass,
        'posts' : posts,
    }

    return render(request, 'classPage.html', response)

def aboutPage(request):
    return render(request, 'aboutPage.html')

def servicesPage(request):
    return render(request, 'servicesPage.html')

def lecturerPage(request):
    return render(request, 'lecturerPage.html')

#  def contactPage(request):
    #  return render(request, 'contactPage.html')
