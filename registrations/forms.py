from django.forms import ModelForm

from .models import Registration

class AcceptanceForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ('event', 'participant', 'date_registered', 'parents_permit', 'parents_contact_number', 'waiver')