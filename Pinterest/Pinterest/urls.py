"""
URL configuration for Pinterest project.

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
from django.urls import path, include
from reg.views import register

import reg.views as views_reg

urlpatterns = [
    path('', views_reg.home, name='home'),
    path('admin/', admin.site.urls),
    path("reg/", include("allauth.urls")),
    path('register/', register, name='register'),
    path('accounts/google/login/callback/', views_reg.callback_view, name='google_callback'),
]
