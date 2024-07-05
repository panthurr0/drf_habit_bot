from django.urls import path

from habit.apps import HabitConfig
from habit.views import (HabitCreateApiView, HabitDestroyApiView,
                         HabitListApiView, HabitRetrieveApiView,
                         HabitUpdateApiView, MyHabitListApiView)

app_name = HabitConfig.name

urlpatterns = [
    path("habit/create", HabitCreateApiView.as_view(), name="habit-create"),
    path("habit/", HabitListApiView.as_view(), name="habit-list"),

    path("habit/my",
         MyHabitListApiView.as_view(),
         name="habit-list"
         ),
    path(
        "habit/<int:pk>",
        HabitRetrieveApiView.as_view(),
        name="habit-detail"
    ),
    path(
        "habit/update/<int:pk>",
        HabitUpdateApiView.as_view(),
        name="habit-update"
    ),
    path(
        "habit/delete/<int:pk>",
        HabitDestroyApiView.as_view(),
        name="habit-delete"
    ),
]
