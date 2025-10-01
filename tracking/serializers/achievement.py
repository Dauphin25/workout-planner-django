from rest_framework import serializers
from ..models.achievement import Achievement
from exercises.serializers.exercise import ExerciseSerializer

class AchievementSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    achievement_context = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = [
            'id', 'user', 'exercise', 'description', 'value',
            'achieved_at', 'notes', 'achievement_context'
        ]

    def get_achievement_context(self, obj):
        return obj.get_achievement_context()

