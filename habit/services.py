from requests import get
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from config import settings


def make_schedule(habit):
    """Создаёт расписание и периодическую таску."""

    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.habit_time.minute,
        hour=habit.habit_time.hour,
        day_of_week="*",
        day_of_month=f"*/{habit.periodicity}",
        month_of_year="*",
    )

    PeriodicTask.objects.create(
        crontab=schedule,
        name=f"Send notification user: {habit.owner}, action: {habit.action}",
        task="habit.tasks.send_notification",
        kwargs={"chat_id": habit.owner.tg_id,
                "message": f"Привет, {habit.owner}! Время для привычки: {habit.action}"},
    )


def send_telegram_message(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params)
