from rest_framework import serializers
from ..models.goal_tracking import GoalTracking
from workout_plan.serializers.goal import GoalSerializer

class GoalTrackingSerializer(serializers.ModelSerializer):
    goal = GoalSerializer(read_only=True)
    goal_summary = serializers.SerializerMethodField()
    progress_percent = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = GoalTracking
        fields = [
            'id', 'user', 'goal', 'target_value', 'current_value',
            'starting_weight', 'ending_weight', 'progress_percent',
            'notes', 'is_achieved', 'started_at', 'achieved_at', 'goal_summary'
        ]

    def get_goal_summary(self, obj):
        return obj.get_goal_summary()

