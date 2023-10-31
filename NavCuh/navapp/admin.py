from django.contrib import admin
from .models import Department,Teacher
# Register your models here.

class DeptartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("dept_name",)}

admin.site.register(Department, DeptartmentAdmin)
admin.site.register(Teacher)
