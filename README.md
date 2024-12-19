# Library Management System -All the API are attached in file named Library Management System

This is a Django-based Library Management System API that allows users to manage books and library members. The system supports operations such as adding, updating, deleting, and retrieving book details, as well as managing library members.

## Features

- **Book Management**: 
  - Add, update, delete, and view books.
  - Each book has a title, author, publication date, ISBN, and availability status.

- **Member Management**: 
  - Add, update, delete, and view library members.
  - Each member has a name and email.

- *

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework 3.12 or higher
- SQLite (default database)
- Postman or any HTTP client to test the API

## Setup Instructions

### Step 1: Clone the Repository

Clone the project repository to your local machine:

git clone https://github.com/ABHISHEKKUMAR707/library-management-system.git

Step 2: Create a Virtual Environment
Navigate to the project folder and create a virtual environment:


cd library_management_system
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

Step 4: Run Migrations
Apply database migrations to set up the necessary tables:


python manage.py migrate
Step 5: Create a Superuser (Optional)
To access the Django admin panel, create a superuser:

python manage.py createsuperuser
Follow the prompts to set up a username, email, and password.

Step 6: Run the Development Server
Start the Django development server:


python manage.py runserver
Your API should now be accessible at http://127.0.0.1:8000/.

API Endpoints

Books
GET /api/books/: List all books.
POST /api/books/: Create a new book.
GET /api/books/{id}/: Get details of a book by ID.
PUT /api/books/{id}/: Update book details by ID.
DELETE /api/books/{id}/: Delete a book by ID.

Members
GET /api/members/: List all members.
POST /api/members/: Create a new member.
GET /api/members/{id}/: Get details of a member by ID.
PUT /api/members/{id}/: Update member details by ID.
DELETE /api/members/{id}/: Delete a member by ID.


