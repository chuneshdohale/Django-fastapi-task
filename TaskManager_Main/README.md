Django Task Management CRUD API
Welcome to the Django Task Management CRUD API documentation! This API allows you to perform CRUD (Create, Read, Update, Delete) operations on tasks.

Project Requirements
To use this API, make sure you have the following installed:

Python 3.9+
SQLite
Project Setup
1. Clone the Repository
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/chuneshdohale/Django-fastapi-task.git
2. Apply Migrations
Run the following commands to apply database migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
3. Run the Development Server
Start the development server with the following command:

bash
Copy code
python manage.py runserver
API Endpoints
1. Get a List of Tasks
Endpoint: /tasks/
Method: GET
Description: Retrieve a list of all tasks.
2. Get a Single Task
Endpoint: /tasks/<task_id>/
Method: GET
Description: Retrieve details of a specific task.
3. Create a New Task
Endpoint: /tasks/
Method: POST
Description: Create a new task.
Request Body:
json
Copy code
{
  "title": "Task Title",
  "description": "Task Description",
  "due_date": "2023-12-31",
  "status": "unstarted"
}
4. Update a Task
Endpoint: /tasks/<task_id>/
Method: PUT
Description: Update details of a specific task.
Request Body:
json
Copy code
{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "due_date": "2023-12-31",
  "status": "finished"
}
5. Delete a Task
Endpoint: /tasks/<task_id>/
Method: DELETE
Description: Delete a specific task.
Explore the API
Feel free to use tools like curl, Postman, or any other API testing tool to interact with these endpoints. Happy coding!