
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Student,Teacher,User



class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_no= forms.CharField(required=True)
    email_id = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self):
        user= super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=User)
        student.phone_no = self.cleaned_data.get('phone_no')
        student.email_id = self.cleaned_data.get('email_id')
        student.save()
        return user
class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_id = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self):
        user= super().save(commit=False)
        user.is_teacher= True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        teacher = Teacher.objects.create(user=User)
        teacher.phone_no = self.cleaned_data.get('phone_no')
        teacher.email_id = self.cleaned_data.get('email_id')
        teacher.save()
        return user