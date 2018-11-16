from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import View, ListView
from .models import Attendance

class AttendanceSummaryView(ListView):
    model = Attendance
    template_name= "event_list.html"
    contex_object_name= "attendance_list"

class AttendanceView(View):
    
    def accept(request):
        if request.method == 'POST':
            return redirect('home')

    def decline(request):
        if request.method == 'POST':
            return redirect('home')
