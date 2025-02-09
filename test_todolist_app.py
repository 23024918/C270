import unittest
from test_todolist_app import app  

class TestToDoListApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        app.tasks = [] 

    def test_get_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to your To-Do List!', response.data) 

    def test_get_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your Tasks', response.data)

    def test_get_task_not_found(self):
        response = self.app.get('/task/1')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Task not found', response.data) 

    def test_add_task(self):
        response = self.app.post('/addTask', data={
            'taskName': 'Test Task',
            'priority': 'High',
            'deadline': '2024-12-31'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/')

    def test_edit_task_not_found(self):
        response = self.app.get('/editTask/1')
        self.assertEqual(response.status_code, 404)

    def test_edit_task(self):
        # Add a task first
        self.app.post('/addTask', data={
            'taskName': 'Initial Task',
            'priority': 'Medium',
            'deadline': '2024-12-20'
        })

        response = self.app.post('/editTask/1', data={ 
            'taskName': 'Updated Task',
            'priority': 'Low',
            'deadline': '2025-01-01'
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_task_not_found(self):
        response = self.app.get('/deleteTask/1')
        self.assertEqual(response.status_code, 302) 

    def test_delete_task(self):
        # Add a task first
        self.app.post('/addTask', data={
            'taskName': 'Task to Delete',
            'priority': 'High',
            'deadline': '2024-12-25'
        })

        response = self.app.get('/deleteTask/1')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()