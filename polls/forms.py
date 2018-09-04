from django import forms
from .models import Student

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('question_text', 'pub_date')


