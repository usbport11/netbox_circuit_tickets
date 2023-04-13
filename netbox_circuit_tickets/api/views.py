from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import CircuitTicketSerializer

class CircuitTicketViewSet(NetBoxModelViewSet):
    queryset = models.CircuitTicket.objects.prefetch_related('tags')
    serializer_class = CircuitTicketSerializer
    filterset_class = filtersets.CircuitTicketFilterSet
