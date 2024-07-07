from celery import shared_task

from habit.services import send_telegram_message


@shared_task
def send_notification(**kwargs):
    """Отправляет уведомление о привычке пользователю в телеграм."""
    chat_id = kwargs["chat_id"]
    message = kwargs["message"]
    send_telegram_message(chat_id, message)

    return f"{message}; Отправлено для {chat_id}"
