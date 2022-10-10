from django.contrib import admin
from test_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
