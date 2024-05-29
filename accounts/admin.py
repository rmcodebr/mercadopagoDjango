from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Group_Permissions, User_Groups, Group

admin.site.register(Group_Permissions)
admin.site.register(User_Groups)
admin.site.register(Group)


class UserAdmin(BaseUserAdmin):
  list_display = ["email", 'role', "is_active"]
  list_filter = ["role"]
  list_editable = ['is_active']
  fieldsets = [
      (None, {"fields": ["email", "password"]}),
      ("Personal Info", {"fields": [
       "first_name", 'last_name', 'phone_number']}),
      ("Financial Info", {"fields": ["mercadopago_customer_id"]}),
      ("Permissions", {"fields": ['role', "is_active", "is_admin"]}),
  ]
  add_fieldsets = [
      (
          None,
          {
              "classes": ["wide"],
              "fields": ["email", 'role', "password1", "password2"],
          },
      ),
  ]

  search_fields = ["email"]
  ordering = ["email"]
  filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
