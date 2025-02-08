import unittest
from unittest.mock import patch
from flask import Flask, render_template, request, redirect, url_for

# Create a mock Flask app for testing
app = Flask()

# Mock MySQL connection (replace with your actual connection handling)
connection = None

# Define test routes and functions
@app.route('/')
def index():
    # Simulate database query
    mock_results = [
        {'taskId': 1, 'tasks': 'Task 1', 'priority': 'High', 'deadline': '2024-12-31'},
        {'taskId': 2, 'tasks': 'Task 2', 'priority': 'Medium', 'deadline': '2024-12-25'}
    ]
    return render_template('index.html', task=mock_results)

@app.route('/addTask', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        tasks = request.form['tasks']
        priority = request.form['priority']
        deadline = request.form['deadline']
        # Simulate database insertion
        return redirect(url_for('index'))
    return render_template('addTask.html')

@app.route('/editTask/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        tasks = request.form['tasks']
        priority = request.form['priority']
        deadline = request.form['deadline']
        # Simulate database update
        return redirect(url_for('index'))
    # Simulate database query to get task details
    mock_task = {'taskId': task_id, 'tasks': 'Existing Task', 'priority': 'Low', 'deadline': '2025-01-15'}
    return render_template('editTask.html', task=mock_task)

@app.route('/deleteTask/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    # Simulate database deletion
    return redirect(url_for('index'))

# Test cases
class TestTaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task 1', response.data)
        self.assertIn(b'Task 2', response.data)

    def test_add_task(self):
        response = self.app.post('/addTask', data={'tasks': 'New Task', 'priority': 'Low', 'deadline': '2025-01-01'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful addition

    def test_edit_task_get(self):
        response = self.app.get('/editTask/1')  # Assuming task with ID 1 exists
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Existing Task', response.data) 

    def test_edit_task_post(self):
        response = self.app.post('/editTask/1', data={'tasks': 'Updated Task', 'priority': 'Medium', 'deadline': '2025-01-10'})
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        response = self.app.get('/deleteTask/1')  # Assuming task with ID 1 exists
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()