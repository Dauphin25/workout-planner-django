from django.db import models
from django.utils.translation import gettext_lazy as _
from .muscle import Muscle


class Exercise(models.Model):
    class Difficulty(models.TextChoices):
        BEGINNER = "beginner", _("Beginner")
        INTERMEDIATE = "intermediate", _("Intermediate")
        ADVANCED = "advanced", _("Advanced")

    class ExerciseType(models.TextChoices):
        STRENGTH = "strength", _("Strength")
        CARDIO = "cardio", _("Cardio")
        FLEXIBILITY = "flexibility", _("Flexibility")
        ENDURANCE = "endurance", _("Endurance")

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text=_("General description of the exercise"))
    instructions = models.TextField(help_text=_("Step-by-step guide to perform the exercise"))
    target_muscles = models.ManyToManyField(
        Muscle,
        related_name="exercises",
        help_text=_("Muscles primarily targeted by this exercise"),
    )
    equipment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Equipment required, if any"),
    )
    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.BEGINNER,
    )
    exercise_type = models.CharField(
        max_length=20,
        choices=ExerciseType.choices,
        default=ExerciseType.STRENGTH,
    )

    calories_burned = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text=_("Estimated calories burned per session"),
    )
    duration = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text=_("Typical duration in seconds"),
    )
    tips = models.TextField(
        blank=True,
        null=True,
        help_text=_("Additional tips or safety notes"),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_difficulty_display()})"
