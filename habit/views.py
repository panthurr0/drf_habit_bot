from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitSerializer
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class HabitListApiView(ListAPIView):
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
