from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Groups, StudentsInfo, TeachersInfo


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'password': forms.TextInput(attrs={'placeholder': 'password'}),
        }


class createGroupForm(forms.ModelForm):

    class Meta:
        model = Groups
        fields = ['group_name', 'group_age']


class createStudentForm(forms.ModelForm):

    class Meta:
        model = StudentsInfo
        fields = ['name', 'second_name', 'father_name', 'date_of_birth', 'coins', 'phone_number', 'group', 'equities']

class changeStudentCoinForm(forms.ModelForm):

    class Meta:
        model = StudentsInfo
        fields = ['coins']

class createTeacherForm(forms.ModelForm):

    class Meta:
        model = TeachersInfo
        fields = ['name', 'second_name', 'phone_number', 'email', 'group', 'is_super_user']

class addStudentForm(forms.Form):
    students = forms.ModelMultipleChoiceField(queryset=StudentsInfo.objects.all())