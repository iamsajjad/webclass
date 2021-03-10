
from django.conf import settings
from django.urls import path, include
# import views from application
from .views import *

urlpatterns = [
    path('', classesPage, name='classesPage'),
    path('classes/', classesPage, name='classesPage'),
    path('classes/new/', createClassPage, name='createClassPage'),
    path('classes/<int:classPrimary>/', classPage, name='classPage'),
    path('about/', aboutPage, name='aboutPage'),
    path('services/', servicesPage, name='servicesPage'),
    path('lecturer/', lecturerPage, name='lecturerPage'),
    #  path('contact/', contactPage, name='contactPage'),
]
