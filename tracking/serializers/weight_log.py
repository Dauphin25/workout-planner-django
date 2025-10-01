from rest_framework import serializers
from ..models.weight_log import WeightLog

class WeightLogSerializer(serializers.ModelSerializer):
    bmi = serializers.DecimalField(max_digits=4, decimal_places=2, required=False)
    body_fat_percent = serializers.DecimalField(max_digits=4, decimal_places=2, required=False)
    profile_summary = serializers.SerializerMethodField()

    class Meta:
        model = WeightLog
        fields = [
            'id', 'user', 'weight_kg', 'bmi', 'body_fat_percent',
            'logged_at', 'notes', 'profile_summary'
        ]

    def get_profile_summary(self, obj):
        return obj.get_profile_summary()

