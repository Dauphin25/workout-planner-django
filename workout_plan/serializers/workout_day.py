from rest_framework import serializers

from ..models import WorkoutExercise
from ..models.workout_day import WorkoutDay
from .workout_exercise import WorkoutExerciseCreateSerializer, WorkoutExerciseAdvancedSerializer

class WorkoutDayCreateSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseCreateSerializer(many=True)

    class Meta:
        model = WorkoutDay
        fields = [
            'id', 'day_of_week', 'order', 'focus_area', 'notes', 'is_rest_day',
            'session_rating', 'calories_burned', 'exercises'
        ]

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout_day = WorkoutDay.objects.create(**validated_data)
        for exercise_data in exercises_data:
            WorkoutExercise.objects.create(workout_day=workout_day, **exercise_data)
        return workout_day

class WorkoutDayAdvancedSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseAdvancedSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutDay
        fields = [
            'id', 'day_of_week', 'order', 'focus_area', 'notes', 'is_rest_day',
            'session_rating', 'calories_burned', 'exercises'
        ]
