from django.contrib import admin
from .models import Student, Signup

# Customizing the display of the Student model in admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('field_of_study',)

# Customizing the display of the Signup model in admin
class SignupAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','password')
    search_fields = ('first_name', 'last_name', 'email','password')

# Register the models with their customized admin configurations
admin.site.register(Student, StudentAdmin)
admin.site.register(Signup, SignupAdmin)
