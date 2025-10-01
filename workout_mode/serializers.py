from rest_framework import serializers
from .models import WorkoutSession, WorkoutSessionExercise

class WorkoutSessionExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSessionExercise
        fields = [
            'id', 'session', 'exercise_name', 'sets', 'repetitions', 'rest_seconds',
            'order', 'is_completed', 'notes', 'completed_at',
            'adjusted_reps', 'adjusted_sets', 'adjusted_rest_seconds'
        ]

class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = WorkoutSessionExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = WorkoutSession
        fields = [
            'id', 'user', 'started_at', 'ended_at', 'is_active', 'exercises'
        ]

