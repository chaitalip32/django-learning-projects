# Django Learning Projects

This repository contains multiple Django applications developed while learning Python and Django. It covers fundamental Django concepts, database operations, CRUD functionality, user authentication, and application development.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap

## Applications

### 1. Recipe Management Application
- Create, Read, Update and Delete (CRUD) recipes.
- User Registration.
- User Login and Logout.
- Authentication-based functionality.
- Manage recipe information.

### 2. Student Management Application
- Student and department data management.
- Django Models and ORM.
- Database relationships.
- Generating sample student data using Faker.

### 3. Other Django Practice Applications
- Additional applications and experiments developed while learning Django.
- Practicing Django views, models, templates and database operations.

## Project Structure

```text
core/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── home/
├── public/
├── recipe/
├── stud/
├── vege/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/chaitalip32/django-learning-projects.git
```

2. Navigate to the project directory:

```bash
cd django-learning-projects
```

3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the environment:

```bash
env\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Apply database migrations:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open the application:

```text
http://127.0.0.1:8000/
```

## Learning Objectives

- Understanding Django project and application structure.
- Creating models and managing databases.
- Performing CRUD operations.
- Implementing user registration and authentication.
- Working with Django ORM.
- Understanding migrations.
- Working with Django templates and views.

## Author

Chaitali Pednekar

GitHub: https://github.com/chaitalip32