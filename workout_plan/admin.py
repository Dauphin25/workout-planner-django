from django.contrib import admin
from .models.goal import Goal
from .models.workout_plan import WorkoutPlan
from .models.workout_week import WorkoutWeek
from .models.workout_day import WorkoutDay
from .models.workout_exercise import WorkoutExercise

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'goal_type', 'status', 'recommended_duration_weeks', 'created_at')
    search_fields = ('name', 'goal_type', 'status')
    list_filter = ('goal_type', 'status')
    readonly_fields = ('created_at', 'updated_at')

class WorkoutDayInline(admin.TabularInline):
    model = WorkoutDay
    extra = 1
    fk_name = 'workout_week'  # Reference to WorkoutWeek

class WorkoutWeekInline(admin.TabularInline):
    model = WorkoutWeek
    extra = 1
    fk_name = 'workout_plan'

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'difficulty', 'progress', 'is_active', 'start_date', 'end_date', 'created_at')
    search_fields = ('title', 'user__username', 'goal__name')
    list_filter = ('difficulty', 'is_active', 'goal', 'start_date', 'end_date')
    inlines = [WorkoutWeekInline]  # Inline weeks, not days
    readonly_fields = ('created_at', 'updated_at')

@admin.register(WorkoutWeek)
class WorkoutWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_plan', 'order', 'notes', 'created_at')
    search_fields = ('workout_plan__title', 'order')
    list_filter = ('workout_plan',)
    inlines = [WorkoutDayInline]  # Inline days in week
    readonly_fields = ('created_at', 'updated_at')

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

@admin.register(WorkoutDay)
class WorkoutDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_week', 'day_of_week', 'focus_area', 'is_rest_day', 'session_rating', 'calories_burned', 'created_at')
    search_fields = ('workout_week__workout_plan__title', 'day_of_week', 'focus_area')
    list_filter = ('focus_area', 'is_rest_day')
    inlines = [WorkoutExerciseInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_day', 'exercise', 'sets', 'repetitions', 'intensity', 'completed', 'order')
    search_fields = ('exercise__name', 'workout_day__workout_plan__title')
    list_filter = ('intensity', 'completed')
    readonly_fields = ()
