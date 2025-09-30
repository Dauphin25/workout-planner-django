from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from users.models.user import User


class Profile(models.Model):
    LIFESTYLE_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('light', 'Lightly Active'),
        ('moderate', 'Moderately Active'),
        ('active', 'Active'),
        ('very_active', 'Very Active'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    DIETARY_CHOICES = [
        ('none', 'None'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('paleo', 'Paleo'),
        ('keto', 'Keto'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    lifestyle = models.CharField(max_length=20, choices=LIFESTYLE_CHOICES, default='moderate')
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    bio = models.TextField(_("Bio"), blank=True, null=True)
    dietary_preference = models.CharField(max_length=20, choices=DIETARY_CHOICES, default='none', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        else:
            if hasattr(instance, 'profile'):
                instance.profile.save()

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")