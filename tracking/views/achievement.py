from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from tracking.models.achievement import Achievement
from tracking.serializers.achievement import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'notes']
    ordering_fields = ['achieved_at', 'value']
    ordering = ['-achieved_at']

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user=user)

