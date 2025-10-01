from rest_framework import serializers
from ..models.muscle import Muscle

class MuscleSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()

    class Meta:
        model = Muscle
        fields = [
            'id', 'name', 'group', 'description', 'origin', 'insertion', 'function', 'summary'
        ]

    def get_summary(self, obj):
        """Return a short summary for display."""
        return f"{obj.name} ({obj.get_group_display()})"
