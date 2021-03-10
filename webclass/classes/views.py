
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

# Create your views here.


@login_required(login_url='/account/')
def createClass(request):

    name     = request.POST.get('name', 'name')
    stage    = request.POST.get('stage', 'stage')

    newPost = Classes.objects.create(owner=str(request.user), name=name,
                                     stage=stage)

    classPrimary = newPost.primary
    newPost.save()

    return HttpResponseRedirect(f'/classes/{classPrimary}/')

@login_required(login_url='/account/')
def deleteClass(request, classPrimary):

    Classes.objects.get(primary=classPrimary).delete()

    return HttpResponseRedirect('/classes/')

@login_required(login_url='/account/')
def createPost(request, classPrimary):

    title    = request.POST.get('title', 'title')
    text     = request.POST.get('text', 'text')
    postFile = request.FILES.get('postFile', 'empty.txt')
    hasFile = True if request.FILES.get('postFile') else False

    newPost = Posts.objects.create(owner=str(request.user), title=title, text=text,
                                   hasFile=hasFile, postFile=postFile)
    Classes.objects.get(primary=classPrimary).posts.add(newPost)
    newPost.save()

    return HttpResponseRedirect(f'/classes/{classPrimary}/')

@login_required(login_url='/account/')
def deletePost(request, classPrimary, postPrimary):

    Posts.objects.get(primary=postPrimary).delete()

    return HttpResponseRedirect(f'/classes/{classPrimary}/')

@login_required(login_url='/account/')
def addComment(request, classPrimary, postPrimary):

    text = request.POST['text']
    newComment = Comments.objects.create(text=text, owner=str(request.user))
    Posts.objects.get(primary=postPrimary).comments.add(newComment)
    newComment.save()

    return HttpResponseRedirect(f'/classes/{classPrimary}/')
