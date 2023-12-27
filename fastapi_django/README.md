# Task Management App API Documentation

This repository contains a Task Management App API built using FastAPI and SQLite as the database. The API provides endpoints to manage tasks including creating, retrieving, updating, and deleting tasks.

## Project Requirements

- Python 3.9+
- sqlite
- FastAPI

## Project Setup

1. **Clone the Repository:**
   Clone this repository to your local machine using the following command:

```bash
    git clone https://github.com/chuneshdohale/Django-fastapi-task.git
```

2. **Install Dependencies:**
   Navigate to the project directory and install the required dependencies using pip:

```bash
cd fast-api-task-management/
pip install -r requirements.txt
```

3. **Run the API:**
   To run the api, navigate to the `apps` folder use the following command:

```bash
cd app/
python3 main.py
```

The API will be accesible on **`http://localhost:8000`**.

## API Endpoints

### Get All Tasks

- **Endpoint:** **`/api/tasks/`**
- **Method:** GET
- **Response:**

```json
{
  "code": "success",
  "status": 200,
  "response": [
    {
      "id": 1,
      "title": "Sample Task",
      "description": "This is a sample task",
      "dueDate": "2019-08-24T14:15:22Z"
    }
    // ... other tasks
  ]
}
```

### Create Task

- **Endpoint:** **`/api/tasks/`**
- **Method:** POST
- **Request:**

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "dueDate": "2023-08-29T15:51:12.999Z"
}
```

- **Response:**

```json
{
  "code": "success",
  "status": 201,
  "response": {
    "id": 0,
    "title": "string",
    "description": "string",
    "dueDate": "2023-08-29T15:51:12.999000Z"
  }
}
```

### Get Task by ID

- **Endpoint:** **`/api/tasks/{task_id}`**
- **Method:** GET
- **Response:**

```json
{
  "code": "success",
  "status": 200,
  "response": {
    "id": 1,
    "title": "string",
    "description": "string",
    "dueDate": "2023-08-28T22:26:23.434000Z"
  }
}
```

### Update Task

- **Endpoint:** **`/api/tasks/{task_id}`**
- **Method:**
- **Request:**

```json
{
  "id": 1,
  "title": "Updated Task",
  "description": "string",
  "dueDate": "2023-08-29T15:51:12.999Z"
}
```

- **Response:**

```json
{
  "code": "success",
  "status": 200,
  "response": {
    "id": 1,
    "title": "Updated Task",
    "description": "string",
    "dueDate": "2023-08-29T15:51:12.999000Z"
  }
}
```

### Delete Task

- **Endpoint:** **`/api/tasks/`**
- **Method:** DELETE
- **Response:**

```json
{
  "code": "success",
  "status": 204,
  "response": "task deleted"
}
```

