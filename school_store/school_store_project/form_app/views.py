from django.shortcuts import render, redirect
from django.contrib import auth
from . models import DOB
# views.py

def form(request):
    return render(request,'form.html')


def submit_order(request):
    # Handle form submission logic here
    # This view will be called when the form is submitted

    # Example logic:
    if request.method == 'POST':
        # Process form data and save to the database, etc.
        # For demonstration, just returning a simple message
        message = "Order Confirmed"
        return render(request, 'confirmation.html', {'message': message})

    # If the form is not submitted via POST, redirect or handle accordingly
    return render(request, 'error.html', {'error_message': 'Invalid form submission'})

from django.http import HttpResponse



