from django.contrib import admin
from .models.achievement import Achievement
from .models.goal_tracking import GoalTracking
from .models.weight_log import WeightLog

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'exercise', 'description', 'value', 'achieved_at', 'notes'
    )
    search_fields = ('user__username', 'exercise__name', 'description', 'value', 'notes')
    list_filter = ('exercise', 'achieved_at')
    readonly_fields = ('achieved_at',)

@admin.register(GoalTracking)
class GoalTrackingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'goal', 'target_value', 'current_value', 'starting_weight',
        'ending_weight', 'progress_percent', 'notes', 'is_achieved', 'started_at', 'achieved_at'
    )
    search_fields = ('user__username', 'goal__name', 'target_value', 'current_value', 'notes')
    list_filter = ('goal', 'is_achieved', 'started_at', 'achieved_at')
    readonly_fields = ('started_at', 'achieved_at', 'progress_percent')

@admin.register(WeightLog)
class WeightLogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'weight_kg', 'bmi', 'body_fat_percent', 'logged_at', 'notes'
    )
    search_fields = ('user__username', 'notes')
    list_filter = ('logged_at',)
    readonly_fields = ('logged_at',)

# Register your models here.
