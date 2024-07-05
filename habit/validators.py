from datetime import timedelta

from rest_framework.exceptions import ValidationError


class RewardValidator:
    """Позволяет выбрать только одно из: linked_habit и reward"""

    def __call__(self, attrs):
        linked_habit = attrs.get("linked_habit")
        reward = attrs.get("reward")
        if linked_habit and reward:
            raise ValidationError(
                "Нельзя одновременно использовать linked_habit и reward"
            )


class CompleteTimeValidator:
    """Проверяет, что время выполнения < 120 секунд"""

    def __call__(self, attrs):
        habit_time = attrs.get("habit_time")
        complete_time = attrs.get("complete_time")

        if habit_time and complete_time:
            habit_timedelta = timedelta(
                hours=habit_time.hour,
                minutes=habit_time.minute,
                seconds=habit_time.second,
            )
            complete_timedelta = timedelta(
                hours=complete_time.hour,
                minutes=complete_time.minute,
                seconds=complete_time.second,
            )
            difference = complete_timedelta - habit_timedelta

            if difference.total_seconds() > 120:
                raise ValidationError(
                    "Разница между habit_time и complete_time должна быть меньше 120 секунд"
                )
            elif difference.total_seconds() < 0:
                raise ValidationError(
                    "Разница между habit_time и complete_time отрицательная"
                )


class LinkedHabitValidator:
    """Проверяет, что в связанные привычки вписана приятная привычка"""

    def __call__(self, attrs):
        habit_item = attrs.get("linked_habit")

        if habit_item and not habit_item.is_nice_habit:
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class IsNiceHabitValidator:
    """Проверяет приятную привычку на вознаграждение или связанную привычку"""

    def __call__(self, attrs):
        is_nice_habit = attrs.get("is_nice_habit")
        if is_nice_habit is True:
            reward = attrs.get("reward")
            linked_habit = attrs.get("linked_habit")
            if reward or linked_habit:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )


class PeriodicityValidator:
    """Проверяет, чтобы привычка выполнялась чаще, чем 1 раз в 7 дней"""

    def __call__(self, attrs):
        periodicity = attrs.get("periodicity")

        if periodicity and periodicity <= 0:
            raise ValidationError("Значение периодичности должно быть > 0")
        if periodicity and periodicity > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
