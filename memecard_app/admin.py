from django.contrib import admin

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    fieldsets = (
        (None, {
            "fields": (
                "username",
            ),
        }),
        ("User Information", {
            "fields": (
                "email",
            ),
        }),
    )
    

admin.site.register(User, UserAdmin)

