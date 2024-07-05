from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    recipe_view_count = models.IntegerField(default=1)


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ["department"]
        verbose_name = "department"


class StudentId(models.Model):
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.student_id


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True
    )
    student_id = models.OneToOneField(
        StudentId, unique=True, on_delete=models.CASCADE, null=True, blank=True
    )
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ["student_name"]
        verbose_name = "student"


class SubjectMarks(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="studentmarks",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True
    )
    marks = models.IntegerField()

    def __str__(self):
        return f"name ={self.student.student_name}, marks={self.subject.subject_name}"

    class Meta:
        unique_together = ["student", "subject"]


class ReportCard(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="studentreportcard",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    student_rank = models.IntegerField()
    date_generated = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ["student", "date_generated"]
