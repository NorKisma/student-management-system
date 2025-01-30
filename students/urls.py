from django.urls import path
from . import views
from .views import student_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('signup/', views.signup, name='signup'),
    path('login/', student_login, name='login'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    # Password reset URLs from Django auth views
    
    
    
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
