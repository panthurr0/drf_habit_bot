from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAdminUser

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from users.permission import IsOwner


class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязывает привычку к текущему пользователю."""
        serializer.save(owner=self.request.user)


class HabitListApiView(ListAPIView):
    """Выводит привычки с is_public=True для всех пользователей."""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class MyHabitListApiView(ListAPIView):
    """Выводит только привычки пользователя."""

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user).order_by("id")


class HabitRetrieveApiView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class HabitUpdateApiView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]
