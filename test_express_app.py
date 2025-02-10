import pytest
import requests

BASE_URL = "http://localhost:3000"

def test_home_page():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Task" in response.text

def test_tasks_page():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert "Task" in response.text

def test_add_task():
    task_data = {
        "tasks": "New Task",
        "priority": "High",
        "deadline": "2025-12-31"
    }
    response = requests.post(f"{BASE_URL}/addTask", data=task_data, allow_redirects=True)
    assert response.status_code == 200
    
    # Verify task was added
    tasks_page = requests.get(f"{BASE_URL}/tasks")
    assert "New Task" in tasks_page.text

def test_edit_task():
    # Assume there is at least one task with ID 1
    updated_task = {
        "taskName": "Updated Task",
        "priority": "Medium",
        "deadline": "2026-01-01"
    }
    response = requests.post(f"{BASE_URL}/editTask/1", data=updated_task, allow_redirects=True)
    assert response.status_code == 200
    
    # Verify task was updated
    tasks_page = requests.get(f"{BASE_URL}/tasks")
    assert "Updated Task" in tasks_page.text

def test_delete_task():
    response = requests.get(f"{BASE_URL}/deleteTask/1", allow_redirects=True)
    assert response.status_code == 200
    
    # Verify task was deleted
    tasks_page = requests.get(f"{BASE_URL}/tasks")
    assert "Updated Task" not in tasks_page.text
