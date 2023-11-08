# Hackathon - Django Task Tracker App

## Overview

This is a web-based task tracker application built using Django. It allows users to manage their tasks by providing features such as adding tasks, updating tasks, deleting tasks, and managing task priorities. The application also includes user authentication, registration, and login/logout functionalities.

## Features

- **Task List:** View a list of tasks.

- **Add Task:** Create new tasks with titles, descriptions, priorities, and due dates.

- **Update Task:** Edit and update existing tasks.

- **Delete Task:** Remove tasks from the list.

- **Task Priority:** Assign priorities to tasks (Low, Medium, High).

- **User Authentication:** Users can register, log in, and log out.

## Project Structure

The project structure includes the following directories and files:

- **.idea:** Configuration files for your development environment.

- **static:** Contains static assets like CSS and JavaScript files.

- **todo:** Django app for managing tasks.

  - **models.py:** Defines the Task model with fields like title, description, priority, date, and user association.

  - **apps.py:** Configuration for the Todo app.

  - **views.py:** Includes views for listing, creating, updating, and deleting tasks, as well as task details.

  - **urls.py:** Defines URL patterns for the Todo app.

- **users:** Django app for user authentication.

- **manage.py:** Django management script.

## Installation and Usage

1. Clone the repository to your local machine:
- git clone https://github.com/gold-amaechi/Hackathon.git
- cd Hackathon

2. Create a virtual environment and install project dependencies:
- python -m venv "your virtual environment name"
- source "your virtual environment name"/bin/activate  # On Windows: venv\Scripts\activate
- pip install -r requirements.txt

3. Apply migrations and create a superuser
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

4. Start the development server:
- python manage.py runserver

5. Open your web browser and navigate to http://localhost:8000 to access the app.

To access the admin panel, log in with your superuser credentials at http://localhost:8000/admin/.

Fell free to contact us if you have any queries.
Happy coding!
