from django.db import models

class Goal(models.Model):
    """Represents a specific fitness goal (e.g., weight loss, muscle gain)."""

    GOAL_TYPE_CHOICES = [
        ("weight_loss", "Weight Loss"),
        ("muscle_gain", "Muscle Gain"),
        ("endurance", "Endurance"),
        ("flexibility", "Flexibility"),
        ("general_health", "General Health"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("abandoned", "Abandoned"),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Goal Name",
        help_text="Name of the fitness goal"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Goal Description",
        help_text="Description of the goal"
    )
    goal_type = models.CharField(
        max_length=30,
        choices=GOAL_TYPE_CHOICES,
        default="other",
        verbose_name="Goal Type",
        help_text="Type/category of the goal"
    )
    recommended_duration_weeks = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Recommended Duration (weeks)",
        help_text="Suggested duration to achieve this goal"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
        verbose_name="Goal Status",
        help_text="Current status of the goal"
    )
    feedback = models.TextField(
        blank=True,
        verbose_name="Goal Feedback",
        help_text="User feedback or notes about the goal"
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
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self):
        return self.name
