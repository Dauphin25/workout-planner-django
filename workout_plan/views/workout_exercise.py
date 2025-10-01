from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.workout_exercise import WorkoutExercise
from ..serializers.workout_exercise import (
    WorkoutExerciseCreateSerializer,
    WorkoutExerciseAdvancedSerializer
)

class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseAdvancedSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return WorkoutExerciseCreateSerializer  # This serializer requires workout_day
        return WorkoutExerciseAdvancedSerializer
