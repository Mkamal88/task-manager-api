# Task Manager API

This is a RESTful API for a simple task management system built using Python and Flask. It supports basic CRUD operations for tasks, as well as filtering tasks by status and priority.

## Development Environment Setup

To set up the development environment, follow these steps:

1. Clone the repository:
```git clone https://github.com/your-username/task-manager-api.git```

2. Navigate to the project directory:
```cd task-manager-api```

3. Create a virtual environment:
```python -m venv env```

4. Activate the virtual environment:
```source env/bin/activate```

5. Install the required packages:
```pip install -r requirements.txt```

## Running the API Server

To run the API server, follow these steps:

1. Start the Flask app:
```python tasks_app.py```

2. The API server should now be running at `http://localhost:5000` or `http://127.0.0.1:5000`.

## Running the Unit Tests

To run the unit tests, follow these steps:

1. Run the test script:
```python test_taks_app.py```


3. The unit tests should now be run, and the results should be displayed in the terminal.

## API Endpoints

The API supports the following endpoints:

- GET /tasks : Retrieve a list of all tasks.
- POST /tasks : Create a new task.
- GET /tasks/<task_id> : Retrieve a specific task by its id.
- PUT /tasks/<task_id> : Update a specific task by its id.
- DELETE /tasks/<task_id> : Delete a specific task by its id.
- GET /tasks?status=<status> : Retrieve a list of tasks filtered by status.
- GET /tasks?priority=<priority> : Retrieve a list of tasks filtered by priority.

















