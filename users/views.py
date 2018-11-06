from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView

from .forms import ParticipantCreationForm

class SignUpView(CreateView):
    form_class = ParticipantCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")