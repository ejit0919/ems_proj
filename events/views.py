from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
from registrations.models import Registration

class HomePageView(TemplateView):
    template_name= "home.html"
     
    def get_context_data(self):
        data = {"event_list" : Event.objects.all()}
        return data

class EventListView(ListView):
    model = Event
    template_name= "event_list.html"
    contex_object_name= "event_list"

class EventDetailView(DetailView, TemplateView):
    model = Event
    template_name = "event_detail.html"

    def get_context_data(self, **kwargs):
        data = {
            "event" : Event.objects.filter(pk=self.kwargs["pk"]).first(),
            "registration" : ""
            }
        if str(self.request.user) != "AnonymousUser":
            data["registration"] = Registration.objects.filter(participant=self.request.user, event_id=self.kwargs["pk"]).first()
        
        return data

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

class MyActivitiesListView(ListView, DeleteView):
    model = Registration
    template_name = "myactivities_list.html"
    
    def get_context_data(self, **kwargs):
        data = {
            "registration_list" : Registration.objects.filter(participant=self.request.user),
            "event_list" : Event.objects.all()
            }
        return data

