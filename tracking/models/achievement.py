from django.db import models
from django.conf import settings
from exercises.models.exercise import Exercise
from django.utils.translation import gettext_lazy as _


class Achievement(models.Model):
    """Records specific exercise achievements (personal bests, milestones)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="achievements",
        verbose_name=_("User")
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="achievements",
        verbose_name=_("Exercise")
    )
    description = models.CharField(
        max_length=255,
        help_text=_("E.g., 'Bench pressed 100kg for 5 reps'"),
        verbose_name=_("Description")
    )
    value = models.CharField(
        max_length=50,
        help_text=_("E.g., 100kg, 10km, 30min"),
        verbose_name=_("Value")
    )
    achieved_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Achieved At")
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_("Additional notes or context"),
        verbose_name=_("Notes")
    )

    class Meta:
        ordering = ["-achieved_at"]
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name}: {self.value}"

    def save(self, *args, **kwargs):
        """
        Auto-populate notes with user.profile info if not provided.
        """
        profile = getattr(self.user, 'profile', None)
        if profile and not self.notes:
            info = []
            if getattr(profile, 'weight', None) is not None:
                info.append(f"Weight: {profile.weight}kg")
            if getattr(profile, 'height', None) is not None:
                info.append(f"Height: {profile.height}cm")
            if getattr(profile, 'age', None) is not None:
                info.append(f"Age: {profile.age}")
            gender = getattr(profile, 'gender', None)
            if gender:
                info.append(f"Gender: {str(gender).capitalize()}")
            self.notes = "; ".join(info)
        super().save(*args, **kwargs)

    def get_achievement_context(self):
        """
        Return achievement context including profile info if available.
        """
        profile = getattr(self.user, 'profile', None)
        return {
            "exercise": self.exercise.name,
            "value": self.value,
            "profile_weight": getattr(profile, 'weight', None) if profile else None,
            "profile_height": getattr(profile, 'height', None) if profile else None,
        }
