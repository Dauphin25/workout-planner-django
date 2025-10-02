from django.db import models
from .workout_plan import WorkoutPlan

class WorkoutWeek(models.Model):
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name="weeks",
        verbose_name="Workout Plan"
    )
    order = models.PositiveIntegerField(
        help_text="Week number in the plan (e.g., 1, 2, 3, 4)",
        verbose_name="Order"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Notes",
        help_text="Optional notes for this week"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("workout_plan", "order")
        ordering = ["order"]
        verbose_name = "Workout Week"
        verbose_name_plural = "Workout Weeks"

    def __str__(self):
        return f"{self.workout_plan.title} - Week {self.order}"

