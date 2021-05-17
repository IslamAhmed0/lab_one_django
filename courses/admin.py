from django.contrib import admin
from .models import Student, Track
# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Info', {'fields':['fname','lname','age','email','img']}],
        ['Scholarship Info', {'fields': ['student_track']}]
    )
    # list_display('fname' ,'lname','age','student_track')
    # list_filter("student_track","fname");


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 7

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent ]



#display in admin panel
admin.site.register(Student,CustomStudent)
admin.site.register(Track,CustomTrack)