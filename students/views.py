from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm
from students.forms import LoginForm

from .models import Signup
from .forms import StudentSignupForm
from django.contrib.auth import authenticate, login



from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))



def signup(request):
    if request.method == "POST":
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "students/signup.html", {"success": True})
    else:
        form = StudentSignupForm()
    
    return render(request, "students/signup.html", {"form": form})




def student_login(request):
    error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=email, password=password)
            
            if user:
                login(request, user)  # Log the user in
                return redirect('index')  # Redirect to a specific page after successful login
            else:
                error = True  # Set error flag if authentication fails
    else:
        form = LoginForm()

    return render(request, "students/login.html", {"form": form, "error": error})



# In views.py




def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                # Send a password reset link (Django handles this automatically)
                form.save(request=request)
                return render(request, 'password_reset_done.html')
            except User.DoesNotExist:
                return render(request, 'password_reset.html', {'form': form, 'error': 'No user with that email address.'})
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

