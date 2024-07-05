from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """
    Модель привычек: В книге хороший пример привычки описывается как
    конкретное действие, которое можно уложить в одно предложение:
    я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

    За каждую полезную привычку необходимо себя вознаграждать или
    сразу после делать приятную привычку. Но при этом привычка не
    должна расходовать на выполнение больше двух минут.
    """

    owner = models.ForeignKey(
        "users.User",
        verbose_name="Создатель привычки",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    place = models.CharField(
        verbose_name="Место привычки", max_length=150, **NULLABLE
    )
    action = models.CharField(verbose_name="Действие", **NULLABLE)
    is_nice_habit = models.BooleanField(
        verbose_name="Признак приятной привычки", default=False
    )
    linked_habit = models.OneToOneField(
        "self",
        verbose_name="Связанная привычка",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    periodicity = models.SmallIntegerField(
        verbose_name="Периодичность в днях", default=1, **NULLABLE
    )
    reward = models.TextField(
        verbose_name="Вознаграждение за выполнение", **NULLABLE
    )
    habit_time = models.TimeField(
        verbose_name="Время привычки", **NULLABLE
    )
    complete_time = models.TimeField(
        verbose_name="Время выполнения", **NULLABLE
    )
    is_public = models.BooleanField(
        verbose_name="Признак публичности", **NULLABLE
    )
    is_active = models.BooleanField(
        verbose_name="Признак активности", **NULLABLE
    )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
