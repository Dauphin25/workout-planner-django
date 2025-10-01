from rest_framework import serializers
from ..models.workout_plan import WorkoutPlan
from .goal import GoalSerializer

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

