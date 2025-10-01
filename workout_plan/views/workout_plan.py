from rest_framework import viewsets, permissions

from ..models.workout_plan import WorkoutPlan
from ..serializers import WorkoutPlanCreateSerializer


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Short-circuit for schema generation (Swagger/OpenAPI)
        if getattr(self, 'swagger_fake_view', False):
            return WorkoutPlan.objects.none()
        # Only return plans for authenticated users
        user = self.request.user
        if not user or not user.is_authenticated:
            return WorkoutPlan.objects.none()
        return WorkoutPlan.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
