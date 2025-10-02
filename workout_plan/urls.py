from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.workout_plan import WorkoutPlanViewSet
from .views.workout_week import WorkoutWeekViewSet
from .views.workout_day import WorkoutDayViewSet

router = DefaultRouter()
router.register(r'plans', WorkoutPlanViewSet, basename='workoutplan')
router.register(r'weeks', WorkoutWeekViewSet, basename='workoutweek')
router.register(r'days', WorkoutDayViewSet, basename='workoutday')

urlpatterns = [
    path('', include(router.urls)),
]
