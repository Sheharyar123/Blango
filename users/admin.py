from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
# Register your models here.

admin.site.site_header = 'Blango Admin Panel'
admin.site.index_title = 'Blango'
admin.site.site_title = 'Blango Administration'


admin.site.register(CustomUser, UserAdmin)
