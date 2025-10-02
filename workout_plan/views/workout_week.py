from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.workout_week import WorkoutWeek
from ..serializers.workout_week import WorkoutWeekCreateSerializer

class WorkoutWeekViewSet(viewsets.ModelViewSet):
    queryset = WorkoutWeek.objects.all()
    serializer_class = WorkoutWeekCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return weeks for plans owned by the authenticated user
        user = self.request.user
        if not user or not user.is_authenticated:
            return WorkoutWeek.objects.none()
        return WorkoutWeek.objects.filter(workout_plan__user=user)

