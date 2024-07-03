from django.contrib import admin
from .models import RequestCall

@admin.register(RequestCall)
class RequestCallAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'timestamp']