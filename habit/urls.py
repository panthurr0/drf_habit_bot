from django.urls import path
from habit.apps import HabitConfig
from habit.views import (
    HabitCreateApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
    HabitDestroyApiView
)

app_name = HabitConfig.name

urlpatterns = [
    path(
        'habit/create',
        HabitCreateApiView.as_view(),
        name='Habit-create'
    ),
    path(
        'habit/',
        HabitListApiView.as_view(),
        name='Habit-list'
    ),
    path(
        'habit/<int:pk>',
        HabitRetrieveApiView.as_view(),
        name='Habit-detail'
    ),
    path(
        'habit/update/<int:pk>',
        HabitUpdateApiView.as_view(),
        name='Habit-update'
    ),
    path(
        'habit/delete/<int:pk>',
        HabitDestroyApiView.as_view(),
        name='Habit-delete'
    ),

]
