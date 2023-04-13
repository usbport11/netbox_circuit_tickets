from rest_framework import serializers

from circuits.api.nested_serializers import NestedProviderSerializer, NestedCircuitSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import CircuitTicket

#
# Nested serializers
#

class NestedCircuitTicketSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_circuit_tickets-api:circuitticket-detail'
    )

    class Meta:
        model = CircuitTicket
        fields = ('id', 'url', 'display', 'name')
#
# Regular serializers
#

class CircuitTicketSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_circuit_tickets-api:circuitticket-detail'
    )

    provider = NestedProviderSerializer()
    circuit = NestedCircuitSerializer()

    class Meta:
        model = CircuitTicket
        fields = (
            'id', 'url', 'display', 'name', 'description', 'status', 'provider', 'circuit', 'start', 'end', 'acknowledged', 'comments', 'tags', 'custom_fields', 
            'created', 'last_updated',
        )
