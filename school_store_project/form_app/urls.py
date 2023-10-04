# urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    # ... other URL patterns ...

    path('form/', views.form, name='form'),
    path('submit_order/', views.submit_order, name='submit_order'),
]
