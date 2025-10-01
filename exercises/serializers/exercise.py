from rest_framework import serializers
from ..models.exercise import Exercise
from .muscle import MuscleSerializer

class ExerciseSerializer(serializers.ModelSerializer):
    target_muscles = MuscleSerializer(many=True, read_only=True)
    difficulty_label = serializers.CharField(source='get_difficulty_display', read_only=True)
    exercise_type_label = serializers.CharField(source='get_exercise_type_display', read_only=True)
    calories_per_minute = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = [
            'id', 'name', 'description', 'equipment', 'difficulty', 'difficulty_label',
            'exercise_type', 'exercise_type_label', 'instructions', 'calories_burned',
            'duration', 'tips', 'target_muscles', 'calories_per_minute',
            'created_at', 'updated_at'
        ]

    def get_calories_per_minute(self, obj):
        """Calculate calories burned per minute if duration and calories are set."""
        if obj.calories_burned and obj.duration and obj.duration > 0:
            return round(obj.calories_burned / (obj.duration / 60), 2)
        return None

class ExerciseListSerializer(serializers.ModelSerializer):
    target_muscles = MuscleSerializer(many=True, read_only=True)
    difficulty_label = serializers.CharField(source='get_difficulty_display', read_only=True)
    exercise_type_label = serializers.CharField(source='get_exercise_type_display', read_only=True)

    class Meta:
        model = Exercise
        fields = [
            'id', 'name', 'equipment', 'difficulty', 'difficulty_label',
            'exercise_type', 'exercise_type_label', 'target_muscles'
        ]
