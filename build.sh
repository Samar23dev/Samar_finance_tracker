#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Create superuser if none exists
python manage.py create_superuser_if_none

# Populate sample data (only runs if no data exists)
python manage.py populate_sample_data
