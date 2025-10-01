from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from tracking.models.goal_tracking import GoalTracking
from tracking.serializers.goal_tracking import GoalTrackingSerializer

class GoalTrackingViewSet(viewsets.ModelViewSet):
    queryset = GoalTracking.objects.all()
    serializer_class = GoalTrackingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['notes']
    ordering_fields = ['started_at', 'progress_percent']
    ordering = ['-started_at']

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user=user)

