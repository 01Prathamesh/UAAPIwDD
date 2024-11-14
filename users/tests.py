import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="password")

def test_register(api_client):
    data = {'username': 'newuser', 'password': 'password', 'phone_number': '9876543210', 'date_of_birth': '1990-01-01'}
    response = api_client.post('/api/register/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

def test_login(api_client, user):
    data = {'username': 'testuser', 'password': 'password'}
    response = api_client.post('/api/login/', data, format='json')
    assert response.status_code == status.HTTP_200_OK

def test_profile(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get('/api/profile/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == user.username
