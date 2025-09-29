from django.db import models
from django.utils import timezone


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="First name",
    )
    last_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Last name",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )  
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
        verbose_name="Created at",
    ) 

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        indexes = [
            models.Index(fields=["last_name", "first_name"], name="teacher_name_idx"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name="Title",
    )
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Code",
    ) 
    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )
    teachers = models.ManyToManyField(
        "Teacher",
        related_name="courses",
        blank=True,
        verbose_name="Teachers",
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
        verbose_name="Created at",
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        indexes = [
            models.Index(fields=["title"], name="course_title_idx"),
        ]

    def __str__(self):
        return f"{self.code} – {self.title}"


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="First name",
    )
    last_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Last name",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )  
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
        verbose_name="Created at",
    )
    # Through model allows future metadata (term, grade, etc.)
    courses = models.ManyToManyField(
        "Course",
        through="Enrollment",
        related_name="students",
        blank=True,
        verbose_name="Courses",
    )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        indexes = [
            models.Index(fields=["last_name", "first_name"], name="student_name_idx"),
            models.Index(fields=["created_at"], name="student_created_idx"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        db_index=True,  
        verbose_name="Student",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        db_index=True, 
        verbose_name="Course",
    )
    enrolled_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
        verbose_name="Enrolled at",
    )

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ("student", "course")
        ordering = ["-enrolled_at"]
        indexes = [
            models.Index(fields=["student", "enrolled_at"], name="enroll_student_dt_idx"),
            models.Index(fields=["course", "enrolled_at"], name="enroll_course_dt_idx"),
        ]

    def __str__(self):
        return f"{self.student} → {self.course}"
