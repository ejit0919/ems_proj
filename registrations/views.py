from django.shortcuts import render

# Create your views here.

from events.models import Event
from .models import Registration
from django.views.generic import TemplateView, CreateView

class RegistrationListView(TemplateView):
    template_name = "registration_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["event"] = Event.objects.filter(pk = self.kwargs['event_pk']).first()
        data["registration_list"] = Registration.objects.filter(event =self.kwargs['event_pk'])
        return data

class JoinEventView(CreateView):
    model = Registration
    fields = ['parents_permit', 'parents_contact_number', 'waiver']
    template_name = "event_join.html"

    def form_valid(self, form):
        form.instance.event = Event.objects.filter(pk=self.kwargs["event_pk"]).first()
        form.instance.participant = self.request.user
        return super().form_valid(form)