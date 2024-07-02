from rest_framework.serializers import ModelSerializer

from habit.models import Habit
from habit.validators import RewardValidator, CompleteTimeValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [RewardValidator(), CompleteTimeValidator()]
