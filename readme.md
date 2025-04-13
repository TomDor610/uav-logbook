# UAV Logbook App

A Django-based application to log and manage UAV flight operations, maintenance, and configurations.

## Features
- PostgreSQL-based backend
- Auto-generated models from existing schema
- Admin interface for managing records
- Ready for API and frontend expansion

## Setup

```bash
git clone <your_repo_url>
cd uav-logbook
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
