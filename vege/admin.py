from django.contrib import admin
from django.db.models import Sum

# Register your models here.

from .models import *

admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)


class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]


admin.site.register(SubjectMarks, SubjectMarksAdmin)


class ReportCardAdmin(admin.ModelAdmin):
    list_display = ["student", "student_rank", "total_marks", "date_generated"]
    ordering = ["student_rank"]
    def total_marks(self, obj):
        return SubjectMarks.objects.filter(student=obj.student).aggregate(total_marks = Sum("marks"))["total_marks"]


admin.site.register(ReportCard, ReportCardAdmin)
