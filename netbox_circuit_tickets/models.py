from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class CircuitTicketStatusTypeChoices(ChoiceSet):
    key = 'CircuitTicket.status'

    CHOICES = [
        ('open', 'Open', 'green'),
        ('hold', 'Hold', 'orange'),
        ('closed', 'Closed', 'indigo'),
        ('reject', 'Reject', 'red'),
    ]

class CircuitTicket(NetBoxModel):
    name = models.CharField(
        max_length=100,
        verbose_name="Ticket Id",
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Short description",
    )
    status = models.CharField(
        max_length=30,
        choices=CircuitTicketStatusTypeChoices,
    )
    provider = models.ForeignKey(
        to='circuits.Provider',
        on_delete=models.CASCADE,
        related_name='+',
        default=None
    )
    circuit = models.ForeignKey(
        to='circuits.Circuit',
        on_delete=models.CASCADE,
        related_name='+',
        default=None
    )
    start = models.DateTimeField(
        max_length=100,
    )
    end = models.DateTimeField(
        max_length=100,
        null=True,
        blank=True,
    )
    acknowledged = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name="Acknowledged?",
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_circuit_tickets:circuitticket', args=[self.pk])

    def get_status_color(self):
        return CircuitTicketStatusTypeChoices.colors.get(self.status)
