from extras.plugins import PluginConfig

class NetBoxCircuitTicketsConfig(PluginConfig):
    name = 'netbox_circuit_tickets'
    verbose_name = ' NetBox Circuit Tickets'
    description = 'Manage circuit service tickets'
    version = '0.1'
    base_url = 'circuit-tickets'
    min_version = '3.3.0'

config = NetBoxCircuitTicketsConfig
