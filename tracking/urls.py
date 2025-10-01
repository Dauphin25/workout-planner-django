from rest_framework.routers import DefaultRouter
from tracking.views.weight_log import WeightLogViewSet
from tracking.views.goal_tracking import GoalTrackingViewSet
from tracking.views.achievement import AchievementViewSet

router = DefaultRouter()
router.register(r'weight-logs', WeightLogViewSet, basename='weight-log')
router.register(r'goal-trackings', GoalTrackingViewSet, basename='goal-tracking')
router.register(r'achievements', AchievementViewSet, basename='achievement')

urlpatterns = router.urls
