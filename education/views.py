from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Teacher, Student, Course
from .forms import StudentCourseForm


class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teachers"


class TeacherDetailView(DetailView):
    model = Teacher
    context_object_name = "teacher"


class StudentListView(ListView):
    model = Student
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"


class CourseListView(ListView):
    model = Course
    context_object_name = "courses"


class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"


def student_enroll(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentCourseForm(request.POST, student=student)
        if form.is_valid():
            form.save()
            return redirect(reverse("education:student_detail", args=[student.pk]))
    else:
        form = StudentCourseForm(student=student)
    return render(
        request, "education/student_enroll.html", {"form": form, "student": student}
    )
