#!/usr/bin/env bash
# exit on error
set -o errexit

# Install frontend dependencies and build the React app
cd frontend
npm install
npm run build
cd ..

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
