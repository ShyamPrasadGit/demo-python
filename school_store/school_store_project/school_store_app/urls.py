import credentials
from credentials import admin
from . import views
from django.urls import path, include
from django.urls import path


urlpatterns = [
    path('', views.demo,name='demo'),

]


