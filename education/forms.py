from django import forms
from .models import Course


class StudentCourseForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        help_text="Select one or more courses.",
    )

    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop("student")
        super().__init__(*args, **kwargs)
        self.fields["courses"].initial = self.student.courses.values_list("pk", flat=True)

    def save(self):
        selected = list(self.cleaned_data.get("courses", []))
        self.student.courses.set(selected)
        return self.student
