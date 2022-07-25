from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('enterstudent/', inputdetails, name='inputdetails'),
    path('ranklist/',ranklist,name='ranklist')
]