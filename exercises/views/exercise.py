from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models.exercise import Exercise
from ..serializers.exercise import ExerciseSerializer, ExerciseListSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all().order_by('-created_at')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['difficulty', 'exercise_type', 'equipment', 'target_muscles']
    search_fields = ['name', 'description', 'equipment', 'instructions', 'tips']
    ordering_fields = ['name', 'difficulty', 'exercise_type', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ExerciseListSerializer
        return ExerciseSerializer

