FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create data directory for SQLite
RUN mkdir -p /data

# Collect static files
RUN python manage.py collectstatic --no-input

# Run migrations and start server
CMD python manage.py migrate && \
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'changeme123')" && \
    gunicorn tiktokshopradar.wsgi:application --bind 0.0.0.0:8000
