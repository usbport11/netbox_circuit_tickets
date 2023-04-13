from netbox.views import generic
from django.db.models import Count
from . import filtersets, forms, models, tables

class CircuitTicketView(generic.ObjectView):
    queryset = models.CircuitTicket.objects.all()

class CircuitTicketListView(generic.ObjectListView):
    queryset = models.CircuitTicket.objects.all()
    table = tables.CircuitTicketTable
    filterset = filtersets.CircuitTicketFilterSet
    filterset_form = forms.CircuitTicketFilterForm

class CircuitTicketEditView(generic.ObjectEditView):
    queryset = models.CircuitTicket.objects.all()
    form = forms.CircuitTicketForm

class CircuitTicketDeleteView(generic.ObjectDeleteView):
    queryset = models.CircuitTicket.objects.all()
