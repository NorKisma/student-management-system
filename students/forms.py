from django import forms
from .models import Student
from .models import Signup
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'field_of_study': 'Field of Study',
      'gpa': 'GPA'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }



class StudentSignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )

    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'email',  'password']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'password': 'Password'
        }
        widgets = {
           
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data
   
def student_login(request):
    error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, "students/login.html", {"form": form, "error": error})
  


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))


      