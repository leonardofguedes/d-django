import pytest
from django.contrib.auth import get_user_model
from app.models import Project, Task, Tag

User = get_user_model()

@pytest.mark.django_db
def test_project_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    project = Project.objects.create(name='Test Project', description='Test Description', created_by=user)
    assert project.name == 'Test Project'
    assert project.description == 'Test Description'
    assert project.created_by == user

@pytest.mark.django_db
def test_task_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    project = Project.objects.create(name='Test Project', description='Test Description', created_by=user)
    task = Task.objects.create(title='Test Task', description='Test Task Description', project=project)
    assert task.title == 'Test Task'
    assert task.description == 'Test Task Description'
    assert task.project == project
    assert task.status == 'Pending'  # Assuming 'Pending' is the default status
