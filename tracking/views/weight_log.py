from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from tracking.models.weight_log import WeightLog
from tracking.serializers.weight_log import WeightLogSerializer

class WeightLogViewSet(viewsets.ModelViewSet):
    queryset = WeightLog.objects.all()
    serializer_class = WeightLogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['notes']
    ordering_fields = ['logged_at', 'weight_kg', 'bmi']
    ordering = ['-logged_at']

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user=user)

