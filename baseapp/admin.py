from django.contrib import admin
from .models import *

admin.site.register(CareerRegistration)


@admin.register(RequestCall)
class RequestCallAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'timestamp']


