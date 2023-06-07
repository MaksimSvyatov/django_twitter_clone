from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister Group
admin.site.unregister(Group)

# Extend User Class

# Mix Profile info into User infj
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields in admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial user
admin.site.unregister(User)

# Register user  anf Profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)