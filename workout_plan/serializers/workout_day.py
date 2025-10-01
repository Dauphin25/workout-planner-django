from rest_framework import serializers
from ..models.workout_day import WorkoutDay

class WorkoutDaySerializer(serializers.ModelSerializer):
    focus_area_label = serializers.CharField(source='get_focus_area_display', read_only=True)

    class Meta:
        model = WorkoutDay
        fields = [
            'id', 'workout_plan', 'day_of_week', 'order', 'focus_area',
            'focus_area_label', 'notes', 'is_rest_day', 'session_rating',
            'calories_burned', 'created_at', 'updated_at'
        ]

