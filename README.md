# Django Real Estate Management System

This is a Django-based library management system capstone project.

Framework : Django~=5.2
Database : PostgreSQL

## Installation

Follow these steps to set up and run the Django Real Estate Management system:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GGurol/RealEstate-Management-Website.git
   ```

2. Navigate to the project directory:

   ```bash
   cd RealEstate-Management-Website
   ```

3. Build the docker and build:

   ```bash
   docker compose up --build -d
   ```

4. Apply database migrations:

   ```bash
   docker compose exec web python manage.py makemigrations
   docker compose exec web python manage.py migrate
   ```

5. Create a superuser to access the admin interface:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. Access the application in your web browser at `http://localhost:8000`.


