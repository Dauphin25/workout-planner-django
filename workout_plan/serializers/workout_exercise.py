from rest_framework import serializers
from exercises.models.exercise import Exercise
from exercises.serializers.exercise import ExerciseListSerializer
from ..models.workout_exercise import WorkoutExercise
from ..models.workout_day import WorkoutDay  # Import WorkoutDay model

class WorkoutExerciseCreateSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    exercise_details = ExerciseListSerializer(source='exercise', read_only=True)
    workout_day = serializers.PrimaryKeyRelatedField(queryset=WorkoutDay.objects.all(), required=True)  # Ensure workout_day is required

    class Meta:
        model = WorkoutExercise
        fields = [
            'id', 'exercise', 'exercise_details', 'sets', 'repetitions',
            'duration_seconds', 'distance_meters', 'rest_seconds', 'notes',
            'order', 'intensity', 'tempo', 'completed', 'feedback',
            'workout_day'  # Ensure this is present and required
        ]

    def validate_intensity(self, value):
        try:
            int_value = int(value)
        except (TypeError, ValueError):
            raise serializers.ValidationError("Intensity must be an integer between 1 and 10.")
        if int_value < 1 or int_value > 10:
            raise serializers.ValidationError("Intensity must be between 1 and 10.")
        return int_value

    def validate_workout_day(self, value):
        if value is None:
            raise serializers.ValidationError("Workout day must be provided.")
        return value

class WorkoutExerciseAdvancedSerializer(serializers.ModelSerializer):
    exercise_details = ExerciseListSerializer(source='exercise', read_only=True)
    total_volume = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutExercise
        fields = [
            'id', 'exercise', 'exercise_details', 'sets', 'repetitions',
            'duration_seconds', 'distance_meters', 'rest_seconds', 'notes',
            'order', 'intensity', 'tempo', 'completed', 'feedback', 'total_volume'
        ]

    def get_total_volume(self, obj):
        # Example: sets * repetitions
        if obj.sets and obj.repetitions:
            return obj.sets * obj.repetitions
        return None

    def validate_intensity(self, value):
        try:
            int_value = int(value)
        except (TypeError, ValueError):
            raise serializers.ValidationError("Intensity must be an integer between 1 and 10.")
        if int_value < 1 or int_value > 10:
            raise serializers.ValidationError("Intensity must be between 1 and 10.")
        return int_value
