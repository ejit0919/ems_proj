from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from . import models, forms
from events.models import Event
from .models import Registration
from users.models import Participant
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, View

from .forms import AcceptanceForm

class RegistrationListView(TemplateView, View):
    template_name = "registration_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["event"] = Event.objects.filter(pk = self.kwargs['event_pk']).first()
        data["registration_list"] = Registration.objects.filter(event_id=data["event"].pk)
        return data

    def get(self, request, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["event"] = Event.objects.filter(pk = self.kwargs['event_pk']).first()
        data["registration_list"] = Registration.objects.filter(event_id=data["event"].pk)
        return render(request, self.template_name, data)


    def post(self, request, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["event"] = Event.objects.filter(pk = self.kwargs['event_pk']).first()
        data["registration_list"] = Registration.objects.filter(event_id=data["event"].pk)
        data["participants"] = Participant.objects.filter(data["registration_list"]["participant"])
        if request.POST['opt'] == 'approve':
            prtcpnt =  data["participants"].filter(pk=request.POST.get('id', '')).first()
            pid = int(prtcpnt[0]["pk"])
            reg = Registration.objects.filter(event=self.kwargs['event_pk'], participant=pid).first()
            reg.update(status="Approved")
        elif request.POST['opt'] == 'disapprove':
            reg = Registration.objects.filter(event=self.kwargs['event_pk']).first()
            reg.update(status="Dispproved")
        return render(request, self.template_name, data)

class JoinEventView(CreateView):
    model = Registration
    fields = ['parents_permit', 'parents_contact_number', 'waiver']
    template_name = "event_join.html"

    def form_valid(self, form):
        form.instance.event = Event.objects.filter(pk=self.kwargs["event_pk"]).first()
        form.instance.participant = self.request.user
        return super().form_valid(form)

class RegistrationDetailView(DetailView, TemplateView):
    model = Registration
    template_name = "registration_detail.html"

    def get_context_data(self, **kwargs):
        data = {
            "registration" : Registration.objects.filter(pk=self.kwargs['pk']).first(),
            "participant" : Participant.objects.filter(event=Registration.objects.filter(event=self.kwargs['pk']).first()).first()
        }
        return data


# def approve(request, pk):
#     reg = Registration.objects.filter(pk=pk).delete()
#     #Registration.objects.filter(pk=pk).update(status="Approved")
#     return HttpResponseRedirect(reverse('/'))

# def disapprove(request, pk):
#     reg = Registration.objects.filter(pk=pk).delete()
#     #Registration.objects.filter(pk=pk).update(status="Disapproved")
#     return HttpResponseRedirect(reverse('/'))

