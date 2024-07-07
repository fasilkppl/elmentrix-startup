from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
import re
from django.contrib import messages

def test(request):
    return render(request, 'baseapp/index.html')

def about(request):
    return render(request, 'baseapp/about.html')

def careers(request):
    return render(request, 'baseapp/careers.html')

def is_valid_phone(phone_number):
    # Regular expression to validate a basic 10-digit phone number
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, phone_number))

def request_call_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        if phone_number and is_valid_phone(phone_number):
            RequestCall.objects.create(phone_number=phone_number)
            # Display success message
            messages.success(request, 'Thank you! Your phone number has been submitted successfully.')
            # Redirect to the index page
            return redirect('/')
        else:
            # Handle case where phone_number is not provided or invalid
            if not phone_number:
                messages.error(request, 'Please enter a phone number.')
            else:
                messages.error(request, 'Please enter a valid 10-digit phone number.')
    
    # Handle GET requests or initial page load here
    return render(request, 'baseapp/index.html')
