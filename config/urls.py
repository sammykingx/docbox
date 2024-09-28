"""
URL configuration for docbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic.base import TemplateView, RedirectView
import authentication.urls


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index_page"),
    path("home/", RedirectView.as_view(pattern_name="index_page", permanent=True)),
    path("about/", TemplateView.as_view(template_name="about.html",), name="about_us"),
    path("contact-us/", TemplateView.as_view(template_name="contact_us.html"), name="contact_us"),
    path("admin/", admin.site.urls),
    path("accounts/", include(authentication.urls)),
    path("dashboard/", TemplateView.as_view(template_name="accounts/dashboard.html"),
         name="user_dashboard"
    ),
]
