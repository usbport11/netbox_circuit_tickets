from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms import DateTimePicker, DynamicModelChoiceField
from circuits.models import Provider, Circuit
from .models import CircuitTicket, CircuitTicketStatusTypeChoices

class CircuitTicketForm(NetBoxModelForm):
    provider = DynamicModelChoiceField(
        queryset=Provider.objects.all()
    )
    circuit = DynamicModelChoiceField(
        queryset=Circuit.objects.all(),
        query_params={
            'provider_id': '$provider',
        }
    )

    class Meta:
        model = CircuitTicket
        fields = ('name', 'description', 'status', 'provider', 'circuit', 'start', 'end', 'acknowledged', 'comments', 'tags')
        widgets = {
            'start': DateTimePicker(),
            'end': DateTimePicker()
        }

class CircuitTicketFilterForm(NetBoxModelFilterSetForm):
    model = CircuitTicket

    name = forms.CharField(
        required=False
    )

    summary = forms.CharField(
        required=False
    )

    provider = forms.ModelMultipleChoiceField(
        queryset=Provider.objects.all(),
        required=False
    )

    circuit = forms.ModelMultipleChoiceField(
        queryset=Circuit.objects.all(),
        required=False,
    )

    status = forms.MultipleChoiceField(
        choices=CircuitTicketStatusTypeChoices,
        required=False
    )

    start = forms.CharField(
        required=False
    )

    end = forms.CharField(
        required=False
    )

    acknowledged = forms.BooleanField(
        required=False
    )
