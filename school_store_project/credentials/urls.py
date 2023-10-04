from . import views
from django.urls import path, include

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form1', views.form1, name='form.html'),
]


