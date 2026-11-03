import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Event, Registration


def index(request):
    """Serve the single-page frontend application."""
    return render(request, "events/index.html")


def event_list(request):
    events = Event.objects.all()

    data = [
        {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "date": event.date.isoformat(),
            "venue": event.venue,
            "capacity": event.capacity,
        }
        for event in events
    ]

    return JsonResponse(data, safe=False)


def event_details(request, event_id):
    try:
        event = Event.objects.get(id=event_id)

        registered_count = Registration.objects.filter(
            event=event,
            status="Registered"
        ).count()

        data = {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "date": event.date.isoformat(),
            "venue": event.venue,
            "capacity": event.capacity,
            "registered": registered_count,
            "available_seats": event.capacity - registered_count,
        }

        return JsonResponse(data)

    except Event.DoesNotExist:
        return JsonResponse(
            {"error": "Event not found"},
            status=404
        )


@csrf_exempt
@require_http_methods(["POST"])
def register_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)

        data = json.loads(request.body)

        name = data.get("user_name")
        email = data.get("email")

        if not name or not email:
            return JsonResponse(
                {"error": "Name and email are required"},
                status=400
            )

        if Registration.objects.filter(
            event=event,
            email=email
        ).exists():
            return JsonResponse(
                {"error": "Already registered"},
                status=409
            )

        registered_count = Registration.objects.filter(
            event=event,
            status="Registered"
        ).count()

        if registered_count >= event.capacity:
            return JsonResponse(
                {"error": "Event is full"},
                status=400
            )

        registration = Registration.objects.create(
            event=event,
            user_name=name,
            email=email
        )

        return JsonResponse(
            {
                "message": "Registration successful",
                "registration_id": registration.id,
            },
            status=201
        )

    except Event.DoesNotExist:
        return JsonResponse(
            {"error": "Event not found"},
            status=404
        )

    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )


@csrf_exempt
@require_http_methods(["POST"])
def cancel_registration(request, registration_id):
    try:
        registration = Registration.objects.get(id=registration_id)

        if registration.status == "Cancelled":
            return JsonResponse(
                {"error": "Registration already cancelled"},
                status=400
            )

        registration.status = "Cancelled"
        registration.save()

        return JsonResponse({"message": "Registration cancelled"})

    except Registration.DoesNotExist:
        return JsonResponse(
            {"error": "Registration not found"},
            status=404
        )
