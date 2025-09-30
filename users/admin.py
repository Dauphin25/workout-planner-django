from django.contrib import admin
from users.models.user import User
from users.models.profile import Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'city', 'date_of_birth', 'registration_date')
    search_fields = ('email', 'username', 'first_name', 'last_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'weight', 'height', 'lifestyle', 'age', 'gender', 'dietary_preference')
    search_fields = ('user__username', 'user__email', 'gender', 'dietary_preference')


