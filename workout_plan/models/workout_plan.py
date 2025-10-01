from django.db import models
from django.conf import settings
from .goal import Goal


class WorkoutPlan(models.Model):
    """Represents a user's personalized workout plan."""

    DIFFICULTY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    VISIBILITY_CHOICES = [
        ("private", "Private"),
        ("public", "Public"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workout_plans",
        verbose_name="Owner"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Plan Title",
        help_text="Name of the workout plan (e.g., Summer Shred, Strength Gain)"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Plan Description",
        help_text="Optional description of the workout plan"
    )
    frequency_per_week = models.PositiveIntegerField(
        default=3,
        verbose_name="Sessions per Week",
        help_text="How many times per week the user trains"
    )
    daily_session_duration = models.PositiveIntegerField(
        verbose_name="Daily Session Duration (min)",
        help_text="Approximate daily session duration in minutes"
    )
    goal = models.ForeignKey(
        Goal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="plans",
        verbose_name="Goal"
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="beginner",
        verbose_name="Difficulty",
        help_text="Difficulty level of the plan"
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Start Date",
        help_text="When the plan starts"
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="End Date",
        help_text="When the plan ends"
    )

    progress = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        verbose_name="Progress (%)",
        help_text="Completion percentage of the plan"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="Is this plan currently active?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Workout Plan"
        verbose_name_plural = "Workout Plans"

    def __str__(self):
        return f"{self.title} ({self.user.username})"

