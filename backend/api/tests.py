"""Проверка доступности списка задач."""
from http import HTTPStatus
from api import models

from django.test import Client, TestCase
"""Проверка доступности списка задач."""


class TaskiAPITestCase(TestCase):
    """Проверка доступности списка задач."""

    def setUp(self):
        """Проверка доступности списка задач."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности списка задач."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания задачи."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
