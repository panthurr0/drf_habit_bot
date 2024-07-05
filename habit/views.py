from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitSerializer
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class HabitListApiView(ListAPIView):
    """Выводит привычки с is_public=True для всех пользователей."""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [AllowAny, ]


class MyHabitListApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitRetrieveApiView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateApiView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
