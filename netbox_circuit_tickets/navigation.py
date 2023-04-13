from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


circuitticket_buttons = [
    PluginMenuButton(
        link='plugins:netbox_circuit_tickets:circuitticket_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_circuit_tickets:circuitticket_list',
        link_text='Circuit Tickets',
        buttons=circuitticket_buttons
    ),
)
