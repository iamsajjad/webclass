
from django.conf import settings
from django.urls import path, include
# import views from application
from .views import *

urlpatterns = [
    path('about/', aboutPage, name='aboutPage'),
    path('contact/', contactPage, name='contactPage'),
    path('services/', servicesPage, name='servicesPage'),
    path('classes/', classesPage, name='classesPage'),
    path('', classesPage, name='classesPage'),
]
