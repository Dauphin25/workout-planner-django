from django.contrib import admin
from .models.exercise import Exercise
from .models.muscle import Muscle

@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'origin', 'insertion')
    search_fields = ('name', 'group', 'origin', 'insertion')
    list_filter = ('group',)

class TargetMuscleInline(admin.TabularInline):
    model = Exercise.target_muscles.through
    extra = 1

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'exercise_type', 'difficulty', 'duration', 'calories_burned', 'created_at', 'updated_at'
    )
    search_fields = ('name', 'description', 'instructions', 'tips')
    list_filter = ('exercise_type', 'difficulty')
    inlines = [TargetMuscleInline]
    filter_horizontal = ('target_muscles',)
    readonly_fields = ('created_at', 'updated_at')
