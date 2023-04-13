from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('circuit-tickets/', views.CircuitTicketListView.as_view(), name='circuitticket_list'),
    path('circuit-tickets/add/', views.CircuitTicketEditView.as_view(), name='circuitticket_add'),
    path('circuit-tickets/<int:pk>/', views.CircuitTicketView.as_view(), name='circuitticket'),
    path('circuit-tickets/<int:pk>/edit/', views.CircuitTicketEditView.as_view(), name='circuitticket_edit'),
    path('circuit-tickets/<int:pk>/delete/', views.CircuitTicketDeleteView.as_view(), name='circuitticket_delete'),
    path('circuit-tickets/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='circuitticket_changelog', kwargs={
        'model': models.CircuitTicket
    }),
)
