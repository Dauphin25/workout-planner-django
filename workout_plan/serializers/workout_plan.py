from rest_framework import serializers
from ..models.workout_plan import WorkoutPlan
from .goal import GoalSerializer
from .workout_day import WorkoutDayCreateSerializer
from .workout_week import WorkoutWeekCreateSerializer

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
    weeks = WorkoutWeekCreateSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = [
            'id', 'title', 'description', 'frequency_per_week', 'daily_session_duration',
            'goal', 'difficulty', 'start_date', 'end_date', 'weeks'
        ]

    def create(self, validated_data):
        weeks_data = validated_data.pop('weeks')
        workout_plan = WorkoutPlan.objects.create(**validated_data)
        for week_data in weeks_data:
            days_data = week_data.pop('days')
            week = workout_plan.weeks.create(**week_data)
            for day_data in days_data:
                day_data['workout_week'] = week
                WorkoutDay.objects.create(**day_data)
        return workout_plan
