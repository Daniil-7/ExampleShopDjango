from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from account.models import User


admin.site.register(User)
"""
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
	pass
"""
