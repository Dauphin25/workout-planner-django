from django.db import models
from .workout_week import WorkoutWeek


class WorkoutDay(models.Model):
    """Represents a specific day in a workout plan."""

    FOCUS_AREA_CHOICES = [
        ("upper_body", "Upper Body"),
        ("lower_body", "Lower Body"),
        ("cardio", "Cardio"),
        ("core", "Core"),
        ("full_body", "Full Body"),
        ("rest", "Rest"),
        ("other", "Other"),
    ]

    workout_week = models.ForeignKey(
        WorkoutWeek,
        on_delete=models.CASCADE,
        related_name="days",
        verbose_name="Workout Week",
        null=True,      # Allow null for migration
        blank=True      # Allow blank in admin/forms
    )
    day_of_week = models.CharField(
        max_length=20,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
            ("Saturday", "Saturday"),
            ("Sunday", "Sunday"),
        ],
        verbose_name="Day of Week"
    )
    order = models.PositiveIntegerField(
        help_text="The order of the day in the plan (e.g., Day 1, Day 2)",
        verbose_name="Order"
    )
    focus_area = models.CharField(
        max_length=20,
        choices=FOCUS_AREA_CHOICES,
        default="other",
        verbose_name="Focus Area",
        help_text="Main focus of this workout day"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Notes",
        help_text="Additional notes for this day"
    )
    is_rest_day = models.BooleanField(
        default=False,
        verbose_name="Is Rest Day",
        help_text="Is this a rest day?"
    )
    session_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Session Rating",
        help_text="User rating for this workout day"
    )
    calories_burned = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Calories Burned",
        help_text="Estimated calories burned in this session"
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
        unique_together = ("workout_week", "day_of_week")
        ordering = ["order"]
        verbose_name = "Workout Day"
        verbose_name_plural = "Workout Days"

    def __str__(self):
        return f"{self.workout_week} - {self.day_of_week}"
