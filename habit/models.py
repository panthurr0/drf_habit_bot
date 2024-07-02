from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(
        "users.User",
        help_text='Создатель привычки',
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    place = models.CharField(
        help_text='Место привычки',
        max_length=150,
        **NULLABLE
    )
    habit_time = models.TimeField(
        help_text='Время привычки', **NULLABLE
    )
    action = models.CharField(
        help_text='Действие', **NULLABLE
    )
    is_nice_habit = models.BooleanField(
        help_text='Признак приятной привычки', **NULLABLE
    )
    linked_habit = models.OneToOneField(
        'self',
        help_text="Связанная привычка",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    periodicity = models.SmallIntegerField(
        help_text='Периодичность в днях',
        default=1,
        **NULLABLE
    )
    reward = models.TextField(
        help_text='Вознаграждение за выполнение', **NULLABLE
    )
    complete_time = models.TimeField(
        help_text='Время выполнения', **NULLABLE
    )
    is_public = models.BooleanField(
        verbose_name='Признак публичности', **NULLABLE
    )
    is_active = models.BooleanField(
        verbose_name='Признак активности', **NULLABLE
    )

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
