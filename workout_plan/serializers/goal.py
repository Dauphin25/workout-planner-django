from rest_framework import serializers
from ..models.goal import Goal

class GoalSerializer(serializers.ModelSerializer):
    status_label = serializers.CharField(source='get_status_display', read_only=True)
    goal_type_label = serializers.CharField(source='get_goal_type_display', read_only=True)

    class Meta:
        model = Goal
        fields = [
            'id', 'name', 'description', 'goal_type', 'goal_type_label',
            'recommended_duration_weeks', 'status', 'status_label',
            'feedback', 'created_at', 'updated_at'
        ]

