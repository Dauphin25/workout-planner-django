from rest_framework import serializers
from ..models.workout_exercise import WorkoutExercise
from exercises.serializers.exercise import ExerciseSerializer

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    intensity_label = serializers.CharField(source='get_intensity_display', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = [
            'id', 'workout_day', 'exercise', 'sets', 'repetitions',
            'duration_seconds', 'distance_meters', 'rest_seconds', 'notes',
            'order', 'intensity', 'intensity_label', 'tempo', 'completed',
            'feedback'
        ]

