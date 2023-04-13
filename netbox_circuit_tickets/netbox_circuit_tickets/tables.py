import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import CircuitTicket

class CircuitTicketTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    provider = tables.Column(
        linkify=True
    )
    circuit = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = CircuitTicket
        fields = ('pk', 'id', 'name', 'provider', 'circuit', 'description', 'status',  'start', 'end', 'acknowledged', 'actions')
        default_columns = ('name', 'provider', 'circuit', 'description', 'status', 'start', 'end', 'acknowledged', 'actions')
