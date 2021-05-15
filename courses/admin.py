from django.contrib import admin
from .models import Student, Track
# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Info', {'fields':['fname','lname','age']}],
        ['Scholarship Info', {'fields': ['student_track']}]
    )
    # list_display('fname' ,'lname','age','student_track')

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 5

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent ]


admin.site.register(Student,CustomStudent)
admin.site.register(Track,CustomTrack)