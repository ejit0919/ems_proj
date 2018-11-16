from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import View, ListView
from .models import Attendance

class AttendanceSummaryView(ListView):
    model = Attendance
    template_name= "attendance_summary.html"
    contex_object_name= "attendance_list"

class AttendanceEventDatesView(ListView):
    model = Attendance
    template_name= "attendance_event_dates.html"
    contex_object_name= "attendance_list"

class AttendanceView(View):
    
    def accept(request):
        if request.method == 'POST':
            return redirect('home')

    def decline(request):
        if request.method == 'POST':
            return redirect('home')

