"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from baseapp import views as baseappviews
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', baseappviews.index, name='index'),
    path('request-call/', baseappviews.request_call_view, name='request_call'),
    path('about/', baseappviews.about, name='about'),
    path('careers/', baseappviews.careers, name='careers'),
    path('register/', baseappviews.register_career, name='register_career'),
    path('success/', baseappviews.career_success, name='career_success'),

]


def custom_404(request, exception):
    return render(request, 'baseapp/404.html', status=404)
handler404 = custom_404



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)