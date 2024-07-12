from django import forms
from .models import CareerRegistration

class CareerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CareerRegistration
        fields = ['name', 'email']
