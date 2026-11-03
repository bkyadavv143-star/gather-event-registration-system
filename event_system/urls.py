"""
URL configuration for event_system project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("events.urls")),   # REST API  →  /api/...
    path("", include("events.urls")),       # Frontend  →  /
]
