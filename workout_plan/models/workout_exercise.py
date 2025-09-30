from django.db import models
from exercises.models.exercise import Exercise
from .workout_day import WorkoutDay


class WorkoutExercise(models.Model):
    """Represents a specific exercise inside a workout day, with user customizations."""

    INTENSITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    workout_day = models.ForeignKey(
        WorkoutDay,
        on_delete=models.CASCADE,
        related_name="exercises",
        verbose_name="Workout Day"
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="workout_entries",
        verbose_name="Exercise"
    )
    sets = models.PositiveIntegerField(
        default=3,
        help_text="Number of sets",
        verbose_name="Sets"
    )
    repetitions = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Reps per set if applicable",
        verbose_name="Repetitions"
    )
    duration_seconds = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Duration in seconds for time-based exercises",
        verbose_name="Duration (seconds)"
    )
    distance_meters = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Distance in meters for cardio exercises",
        verbose_name="Distance (meters)"
    )
    rest_seconds = models.PositiveIntegerField(
        default=60,
        help_text="Rest between sets in seconds",
        verbose_name="Rest (seconds)"
    )
    notes = models.TextField(
        blank=True,
        help_text="User notes or modifications",
        verbose_name="Notes"
    )
    order = models.PositiveIntegerField(
        default=1,
        help_text="The order of this exercise in the workout day",
        verbose_name="Order"
    )
    intensity = models.CharField(
        max_length=10,
        choices=INTENSITY_CHOICES,
        default="medium",
        verbose_name="Intensity",
        help_text="Intensity level for this exercise"
    )
    tempo = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Tempo",
        help_text="Tempo for the exercise (e.g., 2-1-2)"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="Completed",
        help_text="Has the user completed this exercise?"
    )
    feedback = models.TextField(
        blank=True,
        verbose_name="Feedback",
        help_text="User feedback or rating for this exercise"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Workout Exercise"
        verbose_name_plural = "Workout Exercises"

    def __str__(self):
        return f"{self.exercise.name} in {self.workout_day}"
