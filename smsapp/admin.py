from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Courses, Students, AdminMain,TODO

# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

admin.site.register(AdminMain)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(TODO)