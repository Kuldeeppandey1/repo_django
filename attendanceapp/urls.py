from django.urls import path
from attendanceapp import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    # path('accounts/login/hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),

]
