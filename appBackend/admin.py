from django.contrib import admin
from appBackend.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fono']

admin.site.register(Employee, EmployeeAdmin)