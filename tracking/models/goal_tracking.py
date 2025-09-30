from django.db import models
from django.conf import settings
from workout_plan.models import Goal
from django.utils.translation import gettext_lazy as _


class GoalTracking(models.Model):
    """Tracks a user's progress toward a fitness goal (e.g., reach 70kg, bench press 100kg)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="goal_progress",
        verbose_name=_("User")
    )
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name="goal_trackings",
        verbose_name=_("Goal")
    )
    target_value = models.CharField(
        max_length=100,
        help_text=_("E.g., 70kg, 10km run, 100 pushups"),
        verbose_name=_("Target Value")
    )
    current_value = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Current Value")
    )
    starting_weight = models.FloatField(
        blank=True,
        null=True,
        help_text=_("Weight at start of goal tracking"),
        verbose_name=_("Starting Weight")
    )
    ending_weight = models.FloatField(
        blank=True,
        null=True,
        help_text=_("Weight at achievement or end"),
        verbose_name=_("Ending Weight")
    )
    progress_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        help_text=_("Progress towards goal (%)"),
        verbose_name=_("Progress (%)")
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_("Additional notes or context"),
        verbose_name=_("Notes")
    )
    is_achieved = models.BooleanField(
        default=False,
        verbose_name=_("Is Achieved")
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Started At")
    )
    achieved_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Achieved At")
    )

    class Meta:
        verbose_name = _("Goal Tracking")
        verbose_name_plural = _("Goal Trackings")

    def __str__(self):
        return f"{self.user.username} tracking {self.goal.name}"

    def save(self, *args, **kwargs):
        """
        Auto-populate starting/ending weight from user.profile if not provided.
        """
        profile = getattr(self.user, 'profile', None)
        if profile:
            if not self.starting_weight and getattr(profile, 'weight', None) is not None:
                self.starting_weight = profile.weight
            if self.is_achieved and not self.ending_weight and getattr(profile, 'weight', None) is not None:
                self.ending_weight = profile.weight
        self.progress_percent = self.calculate_progress()
        super().save(*args, **kwargs)

    def calculate_progress(self):
        """
        Calculate progress percent based on target and current value.
        """
        try:
            if self.target_value and self.current_value:
                target = float(''.join(filter(str.isdigit, self.target_value)))
                current = float(''.join(filter(str.isdigit, self.current_value)))
                if target and current:
                    return round(min(100, (current / target) * 100), 2)
        except (ValueError, TypeError):
            pass
        return 0.0

    def get_goal_summary(self):
        """
        Return goal summary including profile weight if available.
        """
        profile = getattr(self.user, 'profile', None)
        return {
            "goal": self.goal.name,
            "target_value": self.target_value,
            "current_value": self.current_value,
            "starting_weight": self.starting_weight,
            "ending_weight": self.ending_weight,
            "profile_weight": getattr(profile, 'weight', None) if profile else None,
        }
