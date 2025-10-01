from rest_framework import serializers
from ..models.workout_plan import WorkoutPlan
from .goal import GoalSerializer
from .workout_day import WorkoutDayCreateSerializer

class WorkoutPlanSerializer(serializers.ModelSerializer):
    goal = GoalSerializer(read_only=True)
    difficulty_label = serializers.CharField(source='get_difficulty_display', read_only=True)
    visibility_label = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutPlan
        fields = [
            'id', 'user', 'title', 'description', 'frequency_per_week',
            'daily_session_duration', 'goal', 'difficulty', 'difficulty_label',
            'start_date', 'end_date', 'progress', 'is_active',
            'created_at', 'updated_at', 'visibility_label'
        ]

    def get_visibility_label(self, obj):
        # If you add a visibility field, this will display its label
        if hasattr(obj, 'get_visibility_display'):
            return obj.get_visibility_display()
        return None

class WorkoutPlanCreateSerializer(serializers.ModelSerializer):
    days = WorkoutDayCreateSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = [
            'id', 'title', 'description', 'frequency_per_week', 'daily_session_duration',
            'goal', 'difficulty', 'start_date', 'end_date', 'days'
        ]

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        workout_plan = WorkoutPlan.objects.create(**validated_data)
        for day_data in days_data:
            exercises_data = day_data.pop('exercises')
            workout_day = workout_plan.days.create(**day_data)
            for exercise_data in exercises_data:
                workout_day.exercises.create(**exercise_data)
        return workout_plan
