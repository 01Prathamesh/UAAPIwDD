# User Authentication API with Docker and Django

This project provides a Django-based User Authentication API with JWT authentication, user registration, login, and profile management. The application is Dockerized and uses PostgreSQL as the database. It also includes pytest-based unit tests for the authentication endpoints.

## Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [Project Structure](#project-structure)
3. [Endpoints](#endpoints)
4. [Testing](#testing)
5. [Docker Setup](#docker-setup)
6. [Final Notes](#final-notes)

---

## Setup Instructions

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository
    
    ```bash
        git clone https://github.com/01Prathamesh/UAAPIwDD.git
        cd UAAPIwDD

### 2. Set up the Virtual Environment

        I recommend using a virtual environment to isolate dependencies.
        
        ```bash
                python3 -m venv env
                source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install Dependencies
Install all the necessary dependencies using pip.
        ```bash
        pip install -r requirements.txt

### 4. Configure PostgreSQL Database
- Ensure you have PostgreSQL installed and running, or use Docker to run the database.

- Create a new PostgreSQL database or use the one specified in the docker-compose.yml.

### 5. Apply Database Migrations
Run Django migrations to set up the database:
        ```bash
        python manage.py migrate

### 6. Create a Superuser (Optional)
To access the Django admin interface, create a superuser.
        ```bash
        python manage.py createsuperuser

## Project Structure
Here’s a high-level overview of the project structure:
UAAPIwDD/
│
├── users/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tests.py
│   ├── middleware.py
│
├── UAAPIwDD/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## Endpoints
This API exposes the following endpoints for user authentication and profile management:

1. POST /api/register/
Description: Register a new user.

Request Body:
        ```json
        {
        "username": "newuser",
        "password": "password123",
        "phone_number": "9876543210",
        "date_of_birth": "1990-01-01"
        }

Response:
        ```json
        {
            "message": "User created successfully"
        }

2. POST /api/login/
Description: Log in and get a JWT token pair (access and refresh).

Request Body:
        ```json
        Copy code
        {
        "username": "newuser",
        "password": "password123"
        }

Response:
        ```json
        Copy code
        {
        "access": "access_token",
        "refresh": "refresh_token"
        }

3. GET /api/profile/
Description: View the authenticated user's profile (requires JWT authentication).

Headers:
        ```makefile
        Authorization: Bearer <access_token>

Response:
        ```json
        Copy code
        {
        "username": "newuser",
        "phone_number": "9876543210",
        "date_of_birth": "1990-01-01",
        "last_login_ip": "192.168.1.1"
        }

## Testing
This project includes unit tests written with pytest and pytest-django for the following functionalities:

- User registration
- User login (JWT authentication)
- Profile access for authenticated users

1. Install pytest and pytest-django
If not already installed, use the following command to install the necessary testing dependencies:
        ```bash
        pip install pytest pytest-django

2. Run Tests
To run the test suite, use the following command:
        ```bash
        pytest

## Docker Setup
This project is Dockerized, allowing you to run it in containers. Follow the steps below to set up Docker and Docker Compose.

1. Build and Run with Docker
To build and run the application in Docker containers, use the following command:
        ```bash
        docker-compose up --build

This will:
- Build the Docker image for the web application.
- Start the web application and PostgreSQL database in separate containers.

By default, the application will be available at http://localhost:8000.

2. Docker Compose Configuration
The project uses Docker Compose to manage multiple services. The docker-compose.yml file defines two services:

- db: A PostgreSQL database.
- web: The Django application.

Make sure the docker-compose.yml is configured to connect the web service to the db service.

3. Accessing the Application
Once the application is running, you can access the following endpoints:

- Admin Panel: http://localhost:8000/admin (use the superuser credentials).
- API Endpoints: As defined above.

## Final Notes
- Ensure that the PostgreSQL service is up and running, either locally or via Docker.
- The application uses JWT tokens for authentication. When logging in, you will receive an access token that must be included in the Authorization header for protected routes.
- Docker is optional, but recommended for setting up the environment easily.

## .gitignore
Make sure to include the following in your .gitignore to avoid committing unnecessary files:
        ```bash
        __pycache__/
        env/
        *.pyc
        *.pyo
        *.pyd
        db.sqlite3
        *.log

## LICENSE

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.