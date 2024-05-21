import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from app.models import Project, Task, Tag

User = get_user_model()

@pytest.mark.django_db
def test_add_member_to_project():
    client = APIClient()
    creator = User.objects.create_user(username='creator', password='testpassword')
    user = User.objects.create_user(username='member', password='testpassword')
    project = Project.objects.create(name='Test Project', description='Test Description', created_by=creator)
    client.force_authenticate(user=creator)

    url = reverse('project-add-member', args=[project.id])
    response = client.post(url, {'user_id': user.id}, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['status'] == 'Usuário adicionado com sucesso'

@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    user = User.objects.create_user(username='member', password='testpassword')
    project = Project.objects.create(name='Test Project', description='Test Description', created_by=user)
    project.members.add(user)
    client.force_authenticate(user=user)
    
    url = reverse('task-list')
    data = {
        'title': 'New Task',
        'description': 'Task Description',
        'status': 'Pending',
        'project': project.id,
        'tags': [{'title': 'Tag1'}, {'title': 'Tag2'}]
    }
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == 'New Task'
    assert len(response.data['tags']) == 2
