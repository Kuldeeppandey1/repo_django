from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

# # @login_required
# def mark_attendance(request):
#     # Logic to mark attendance
#     return render(request, 'mark_attendance.html')

# # @login_required
# def hr_dashboard(request):
#     # Logic to display HR dashboard
#     return render(request, 'hr_dashboard.html')\

def login(request):
    return render(request, 'login.html')

