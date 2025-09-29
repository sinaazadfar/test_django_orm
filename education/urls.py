from django.urls import path
from . import views

app_name = "education"

urlpatterns = [
    path("teachers/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view(), name="teacher_detail"),

    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("students/<int:pk>/enroll/", views.student_enroll, name="student_enroll"),

    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
]
