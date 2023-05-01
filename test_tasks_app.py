import unittest
import json
from tasks_app import app


class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_get_task(self):
        response = self.app.get('/tasks/1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)

    def test_create_task(self):
        task_data = {
            "title": "Created Task",
            "description": "This is a created task",
            "status": "started",
            "priority": "high",
            "due_date": "2023-05-01"
        }
        response = self.app.post('/tasks', json=task_data)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['title'], task_data['title'])
        self.assertEqual(data['description'], task_data['description'])
        self.assertEqual(data['status'], task_data['status'])
        self.assertEqual(data['priority'], task_data['priority'])
        self.assertEqual(data['due_date'], task_data['due_date'])

    def test_update_task(self):
        task_data = {
            "title": "Updated Task",
            "description": "This is an updated task",
            "status": "completed",
            "priority": "high",
            "due_date": "2023-05-2"
        }
        response = self.app.put('/tasks/1', json=task_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['title'], task_data['title'])
        self.assertEqual(data['description'], task_data['description'])
        self.assertEqual(data['status'], task_data['status'])
        self.assertEqual(data['priority'], task_data['priority'])
        self.assertEqual(data['due_date'], task_data['due_date'])

    def test_delete_task(self):
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 204)

    def test_get_tasks_by_status(self):
        response = self.app.get('/tasks?status=completed')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        for task in data:
            self.assertEqual(task['status'], 'completed')

    def test_get_tasks_by_priority(self):
        response = self.app.get('/tasks?priority=high')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        for task in data:
            self.assertEqual(task['priority'], 'high')


if __name__ == '__main__':
    unittest.main()
