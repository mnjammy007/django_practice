from faker import Faker
import random
from django.db.models import Sum
from .models import Department, StudentId, Student, Subject, SubjectMarks, ReportCard

fake = Faker()


def seed_db(n=10) -> None:
    try:
        department_objs = Department.objects.all()
        for i in range(n):
            department = random.choice(department_objs)
            student_id = f"STU-{fake.random_number(digits=4)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 25)
            student_address = fake.address()

            student_id_obj = StudentId.objects.create(student_id=student_id)
            student_obj = Student.objects.create(
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
                department=department,
            )
    except Exception as e:
        print(e)


def create_subject_marks() -> None:
    try:
        student_objs = Student.objects.all()
        subject_objs = Subject.objects.all()
        for student in student_objs:
            for subject in subject_objs:
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0, 100),
                )
    except Exception as e:
        print(e)


def generate_report_card() -> None:
    try:
        ranks = Student.objects.annotate(
            total_marks=Sum("studentmarks__marks")
        ).order_by("-total_marks", "-student_age")
        for rank in ranks:
            ReportCard.objects.create(
                student=rank,
                student_rank=list(ranks).index(rank) + 1,
            )
    except Exception as e:
        print(e)
