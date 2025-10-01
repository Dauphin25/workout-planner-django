from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.workout_day import WorkoutDay
from ..serializers.workout_day import (
    WorkoutDayCreateSerializer,
    WorkoutDayAdvancedSerializer
)

class WorkoutDayViewSet(viewsets.ModelViewSet):
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDayAdvancedSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WorkoutDayCreateSerializer
        return WorkoutDayAdvancedSerializer
