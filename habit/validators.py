from datetime import timedelta

from rest_framework.exceptions import ValidationError


class RewardValidator:
    """ Позволяет выбрать только одно из: linked_habit и reward """

    def __call__(self, attrs):
        linked_habit = attrs.get('linked_habit')
        reward = attrs.get('reward')
        if linked_habit and reward:
            raise ValidationError('Нельзя одновременно использовать linked_habit и reward')


class CompleteTimeValidator:
    """ Проверяет, что время выполнения < 120 секунд """

    def __call__(self, attrs):
        habit_time = attrs.get('habit_time')
        complete_time = attrs.get('complete_time')

        habit_timedelta = timedelta(hours=habit_time.hour, minutes=habit_time.minute, seconds=habit_time.second)
        complete_timedelta = timedelta(hours=complete_time.hour, minutes=complete_time.minute,
                                       seconds=complete_time.second)

        difference = habit_timedelta - complete_timedelta
        if difference > timedelta(seconds=120):
            raise ValidationError('Разница между habit_time и complete_time должна быть меньше 120 секунд')
