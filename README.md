# TikTok Shop Radar - Waitlist Landing Page

A simple Django waitlist landing page for collecting emails.

## Setup Instructions

### 1. Install Dependencies

First, create a virtual environment and install Django:

```bash
# Install python3-venv if needed (Ubuntu/Debian)
sudo apt install python3-venv

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Django
pip install Django
```

### 2. Make Migrations

Create the database tables:

```bash
# Make migrations for the waitlist app
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 3. Create Superuser (Optional)

To access the admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 4. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

## Project Structure

```
tiktokshopradar/
├── manage.py
├── db.sqlite3 (created after migration)
├── tiktokshopradar/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── waitlist/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── waitlist/
│       └── index.html
└── static/
    └── waitlist/
        └── styles.css
```

## Features

- ✅ Email collection with validation
- ✅ Duplicate email detection
- ✅ Success/error messages using Django messages framework
- ✅ CSRF protection
- ✅ Mobile-first responsive design
- ✅ Clean gradient purple-to-red styling
- ✅ Admin panel for viewing submissions

## Technologies Used

- Django 5.0
- SQLite database
- Django templates
- Pure CSS (no frameworks)
