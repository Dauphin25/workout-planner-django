from django.db import models
from django.utils.translation import gettext_lazy as _


class Muscle(models.Model):
    class MuscleGroup(models.TextChoices):
        CHEST = "chest", _("Chest")
        BACK = "back", _("Back")
        SHOULDERS = "shoulders", _("Shoulders")
        ARMS = "arms", _("Arms")
        CORE = "core", _("Core")
        LEGS = "legs", _("Legs")
        GLUTES = "glutes", _("Glutes")
        FULL_BODY = "full_body", _("Full Body")

    name = models.CharField(max_length=50, unique=True)
    group = models.CharField(
        max_length=20,
        choices=MuscleGroup.choices,
        help_text=_("General muscle group this muscle belongs to"),
    )
    description = models.TextField(blank=True, help_text=_("Optional description of this muscle"))
    origin = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Origin point of the muscle"),
    )
    insertion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Insertion point of the muscle"),
    )
    function = models.TextField(
        blank=True,
        null=True,
        help_text=_("Primary function of the muscle"),
    )

    def __str__(self):
        return f"{self.name} ({self.group})"
