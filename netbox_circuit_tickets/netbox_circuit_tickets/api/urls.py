from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_circuit_tickets'

router = NetBoxRouter()
router.register('circuit-tickets', views.CircuitTicketViewSet)

urlpatterns = router.urls
