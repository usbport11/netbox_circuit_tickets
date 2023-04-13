from netbox.filtersets import NetBoxModelFilterSet
from .models import CircuitTicket


class CircuitTicketFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = CircuitTicket
        fields = ('id', 'name', 'description', 'status', 'provider', 'circuit',  'start', 'end', 'acknowledged', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

