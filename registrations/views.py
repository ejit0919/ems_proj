from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from . import models
from events.models import Event
from .models import Registration
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

class RegistrationListView(TemplateView, UpdateView):
    template_name = "registration_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["event"] = Event.objects.filter(pk = self.kwargs['event_pk']).first()
        data["registration_list"] = Registration.objects.filter(event =self.kwargs['event_pk'])
        return data
        
def approve(request, pk):
    reg = Registration.objects.filter(pk=pk).delete()
    #Registration.objects.filter(pk=pk).update(status="Approved")
    return HttpResponseRedirect(reverse('/'))

def disapprove(request, pk):
    reg = Registration.objects.filter(pk=pk).delete()
    #Registration.objects.filter(pk=pk).update(status="Disapproved")
    return HttpResponseRedirect(reverse('/'))

class JoinEventView(CreateView):
    model = Registration
    fields = ['parents_permit', 'parents_contact_number', 'waiver']
    template_name = "event_join.html"

    def form_valid(self, form):
        form.instance.event = Event.objects.filter(pk=self.kwargs["event_pk"]).first()
        form.instance.participant = self.request.user
        return super().form_valid(form)

class RegistrationDetailView(DetailView):
    model = Registration
    template_name = "registration_detail.html"
    context_object_name = "registration"
