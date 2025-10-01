from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutSessionViewSet, WorkoutSessionExerciseViewSet

router = DefaultRouter()
router.register(r'sessions', WorkoutSessionViewSet, basename='workoutsession')
router.register(r'session-exercises', WorkoutSessionExerciseViewSet, basename='workoutsessionexercise')

urlpatterns = [
    path('', include(router.urls)),
]

