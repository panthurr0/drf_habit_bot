from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_filter = ('id', 'action', 'is_active', 'is_public')
