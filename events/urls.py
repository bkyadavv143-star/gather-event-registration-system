from django.urls import path

from . import views

urlpatterns = [
    # Frontend
    path("", views.index),

    # API
    path("api/events/", views.event_list),
    path("api/events/<int:event_id>/", views.event_details),
    path("api/events/<int:event_id>/register/", views.register_event),
    path("api/registrations/<int:registration_id>/cancel/", views.cancel_registration),
]
