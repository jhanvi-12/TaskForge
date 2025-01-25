# TaskForge

This project is a Django Rest Framework (DRF)-based system for managing categories, products, and tasks. It also supports JWT-based authentication, role-based access control, and asynchronous task notifications using Celery and RabbitMQ.

## 🛠 Skills
Python, Django, DRF, Celery, and RabbitMQ.

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)  
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)  
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)  
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)

---

## Features

1. **User Authentication**:
   - JWT-based authentication (login, logout, and token refresh).
   - Admin seeder script to create admin users.
   - User registration and password reset.

2. **Category Management (Admin Only)**:
   - CRUD operations for categories and subcategories.
   - Nested subcategories.
   - Soft delete and recovery.

3. **Product Management (Admin Only)**:
   - CRUD operations for products.
   - Filtering by category and active status.
   - Soft delete and recovery.

4. **Task Management for Normal Users**:
   - CRUD operations for tasks.
   - Task prioritization and status management.
   - Filtering and sorting tasks.

5. **Asynchronous Task Reminders**:
   - Notifications via email 1 hour before a task's due date.
   - Celery and RabbitMQ integration.

6. **Database**:
   - PostgreSQL as the database.

7. **Testing**:
   - Unit tests for critical functionalities.

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/jhanvi-12/TaskForge.git
cd <repository_folder>
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate  # For Linux/Mac
# OR
env\Scripts\activate   # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
1. Install PostgreSQL on your system.
2. Create a database and user:
   ```sql
   CREATE DATABASE task_management;
   CREATE USER task_user WITH PASSWORD 'password';
   ALTER ROLE task_user SET client_encoding TO 'utf8';
   ALTER ROLE task_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE task_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE task_management TO task_user;
   ```

3. Update the `DATABASES` setting in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'task_management',
           'USER': 'task_user',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Admin Seeder Script
Run the following command to create a superuser:
```bash
python manage.py createsuperuser
```

### 7. Start the Development Server
```bash
python manage.py runserver
```
The server will run on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## RabbitMQ and Celery Setup

### 1. Install RabbitMQ
Follow the instructions on [RabbitMQ's official website](https://www.rabbitmq.com/download.html) to install RabbitMQ on your system.

### 2. Start RabbitMQ Server
```bash
rabbitmq-server
```

### 3. Install Celery
Celery is already included in `requirements.txt`. To manually install it:
```bash
pip install celery
```

### 4. Start Celery Worker
Run the following command from the project directory:
```bash
celery -A task_and_product_management.celery_app worker --loglevel=info
```

### 5. Start Celery Beat Scheduler (Optional, if using periodic tasks)
```bash
celery -A task_and_product_management.celery_app beat --loglevel=info
```

---

## Testing the Application

### Run Unit Tests
```bash
python manage.py test
```

---

## OpenAPI/Swagger Documentation

Swagger documentation is available at:
```text
http://127.0.0.1:8000/api/docs/
```

---
