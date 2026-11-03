# Event Registration System

A web-based Event Registration System built with **Django** and **SQLite**.

## Features

- 📋 View all upcoming events
- 🔍 View event details with live seat availability
- ✅ Register for events (duplicate prevention + capacity check)
- ❌ Cancel an existing registration
- 🛠️ Manage events via Django Admin Panel
- 🎨 Clean single-page frontend (no external dependencies)

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3 + Django |
| Database | SQLite |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| API | Django JSON views (REST-style) |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/event-registration-system.git
cd event-registration-system
```

### 2. Install Dependencies

```bash
pip install django
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Create a Superuser

```bash
python manage.py createsuperuser
```

### 5. Run the Server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/events/` | List all events |
| GET | `/api/events/<id>/` | Event details + seat count |
| POST | `/api/events/<id>/register/` | Register for an event |
| POST | `/api/registrations/<id>/cancel/` | Cancel a registration |

### Register Example

```http
POST /api/events/1/register/
Content-Type: application/json

{
    "user_name": "Rahul Kumar",
    "email": "rahul@example.com"
}
```

## Admin Panel

Visit **http://127.0.0.1:8000/admin/** to manage events and registrations.

## Project Structure

```
event_system/         ← Django project config
events/
├── models.py         ← Event & Registration models
├── views.py          ← API + frontend views
├── urls.py           ← URL routing
├── admin.py          ← Admin registration
└── templates/
    └── events/
        └── index.html  ← Single-page frontend
```

## License

MIT
