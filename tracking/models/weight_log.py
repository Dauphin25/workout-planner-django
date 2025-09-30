from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class WeightLog(models.Model):
    """Tracks the user's weight history over time."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="weight_logs",
        verbose_name=_("User")
    )
    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text=_("Weight in kilograms"),
        verbose_name=_("Weight (kg)")
    )
    bmi = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_("Body Mass Index"),
        verbose_name=_("BMI")
    )
    body_fat_percent = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_("Body fat percentage"),
        verbose_name=_("Body Fat (%)")
    )
    logged_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Logged At")
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_("Additional notes or context"),
        verbose_name=_("Notes")
    )

    class Meta:
        ordering = ["-logged_at"]
        verbose_name = _("Weight Log")
        verbose_name_plural = _("Weight Logs")

    def __str__(self):
        return f"{self.user.username} - {self.weight_kg}kg on {self.logged_at.date()}"

    def save(self, *args, **kwargs):
        """
        Auto-populate weight, BMI, and body fat percent from user.profile if not provided.
        """
        profile = getattr(self.user, 'profile', None)
        if profile:
            if not self.weight_kg and profile.weight is not None:
                self.weight_kg = profile.weight
            if not self.bmi and profile.weight is not None and profile.height is not None:
                self.bmi = self.calculate_bmi(profile.weight, profile.height)
            body_fat = getattr(profile, 'body_fat_percent', None)
            if not self.body_fat_percent and body_fat is not None:
                self.body_fat_percent = body_fat
        super().save(*args, **kwargs)

    @staticmethod
    def calculate_bmi(weight, height):
        """
        Calculate BMI given weight (kg) and height (cm).
        Returns BMI rounded to 2 decimals, or None if invalid input.
        """
        if not weight or not height:
            return None
        try:
            height_m = height / 100.0
            return round(weight / (height_m ** 2), 2)
        except (TypeError, ZeroDivisionError):
            return None

    @staticmethod
    def calculate_body_fat(weight, height, age, gender):
        """
        Calculate body fat percentage using the Deurenberg formula.
        Returns body fat percentage rounded to 2 decimals, or None if invalid input.
        """
        bmi = WeightLog.calculate_bmi(weight, height)
        if bmi is None or age is None or gender is None:
            return None
        gender = str(gender).lower()
        if gender == 'male':
            return round(1.20 * bmi + 0.23 * age - 16.2, 2)
        elif gender == 'female':
            return round(1.20 * bmi + 0.23 * age - 5.4, 2)
        return None

    def get_profile_summary(self):
        """
        Return a summary dict of profile info, or None if profile is missing.
        """
        profile = getattr(self.user, 'profile', None)
        if not profile:
            return None
        return {
            "weight": getattr(profile, 'weight', None),
            "height": getattr(profile, 'height', None),
            "age": getattr(profile, 'age', None),
            "gender": str(getattr(profile, 'gender', '')).capitalize() if getattr(profile, 'gender', None) else None,
            "lifestyle": getattr(profile, 'lifestyle', None),
            "dietary_preference": getattr(profile, 'dietary_preference', None),
        }
