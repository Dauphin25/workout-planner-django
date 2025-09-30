from rest_framework import serializers
from users.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'weight',
            'height',
            'lifestyle',
            'age',
            'gender',
            'bio',
            'dietary_preference',
        ]

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
