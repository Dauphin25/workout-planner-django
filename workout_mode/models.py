from django.db import models
from django.conf import settings

class WorkoutSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

class WorkoutSessionExercise(models.Model):
    session = models.ForeignKey(WorkoutSession, related_name='exercises', on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=128)
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField()
    order = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    adjusted_reps = models.PositiveIntegerField(null=True, blank=True)
    adjusted_sets = models.PositiveIntegerField(null=True, blank=True)
    adjusted_rest_seconds = models.PositiveIntegerField(null=True, blank=True)
