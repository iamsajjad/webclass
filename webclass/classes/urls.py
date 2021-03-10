
from django.conf import settings
from django.urls import path, include
# import views from application
from .views import *

urlpatterns = [
    path('createClass/', createClass, name='createClass'),
    path('deleteClass/<int:classPrimary>/', deleteClass, name='deleteClass'),
    path('createPost/<int:classPrimary>/', createPost, name='createPost'),
    path('deletePost/<int:classPrimary>/<int:postPrimary>/', deletePost, name='deletePost'),
    path('addComment/<int:classPrimary>/<int:postPrimary>/', addComment, name='addComment'),
]
