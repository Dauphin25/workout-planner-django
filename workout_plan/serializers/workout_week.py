from rest_framework import serializers
from ..models.workout_week import WorkoutWeek
from .workout_day import WorkoutDayCreateSerializer

class WorkoutWeekCreateSerializer(serializers.ModelSerializer):
    days = WorkoutDayCreateSerializer(many=True)

    class Meta:
        model = WorkoutWeek
        fields = [
            'id', 'order', 'notes', 'days'
        ]

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        week = WorkoutWeek.objects.create(**validated_data)
        for day_data in days_data:
            day_data['workout_week'] = week
            WorkoutDay.objects.create(**day_data)
        return week

