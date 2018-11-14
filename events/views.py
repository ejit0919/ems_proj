from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event

class HomePageView(TemplateView):
    template_name= "home.html"
     
    def get_context_data(self):
        data = {"event_list" : Event.objects.all()}
        return data

class EventListView(ListView):
    model = Event
    template_name= "event_list.html"
    contex_object_name= "event_list"

class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"

class MyEventListView(ListView):
    model = Event
    template_name = "myevent_list.html"
    context_object_name = "event_list"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(creator = self.request.user)

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'image', 'max_slots', 'date_from', 'date_to', 'time_from', 'time_to', 'venue']
    template_name = "event_create.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class UpdateCreateView(UpdateView):
    model = Event
    fields = ['name', 'description', 'image', 'max_slots', 'date_from', 'date_to', 'time_from', 'time_to', 'venue']
    template_name = "event_update.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("myevent_list")