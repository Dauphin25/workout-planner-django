from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.workout_plan import WorkoutPlanViewSet
from .views.workout_exercise import WorkoutExerciseViewSet
from .views.workout_day import WorkoutDayViewSet

router = DefaultRouter()
router.register(r'plans', WorkoutPlanViewSet, basename='workoutplan')
router.register(r'workout-exercises', WorkoutExerciseViewSet, basename='workout-exercise')
router.register(r'workout-days', WorkoutDayViewSet, basename='workout-day')

urlpatterns = [
    path('', include(router.urls)),
]
