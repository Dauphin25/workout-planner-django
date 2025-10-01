from django.contrib import admin
from .models import WorkoutSession, WorkoutSessionExercise

@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'started_at', 'ended_at', 'is_active')
    list_filter = ('is_active', 'started_at', 'ended_at')
    search_fields = ('user__username',)

@admin.register(WorkoutSessionExercise)
class WorkoutSessionExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'session', 'exercise_name', 'sets', 'repetitions', 'rest_seconds',
        'order', 'is_completed', 'completed_at'
    )
    list_filter = ('is_completed', 'completed_at')
    search_fields = ('exercise_name', 'session__user__username')
