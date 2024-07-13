from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testik@materials.py")
        self.habit = Habit.objects.create(
            action="Лежать", is_nice_habit=True, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тестирование создания привычки."""
        url = reverse("habit:habit-create")
        data = {"action": "Бегать", "is_nice_habit": False}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        """Тестирование списка привычек."""
        url = reverse("habit:habit-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_retrieve(self):
        """Тестирование просмотра привычки."""
        url = reverse("habit:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        """Тестирование редактирования привычки."""
        url = reverse("habit:habit-update", args=(self.habit.pk,))
        data = {"action": "Сидеть"}
        response = self.client.patch(url, data)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get("action"), "Сидеть")

    def test_habit_delete(self):
        """Тестирование удаления привычки."""
        url = reverse("habit:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
