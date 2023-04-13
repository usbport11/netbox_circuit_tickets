## netbox_device_tickets

Manage circuit service tickets

Install steps:

1) cd netbox_circuit_tickets
2) systecmtl stop netbox netbox-rq
3) /opt/netbox/venv/bin/activate
4) nano /opt/netbox/netbox/netbox/configuration.py
<pre>PLUGINS = ['netbox_circuit_tickets']</pre>
6) pip3 install .
7) /opt/netbox/netbox/manage.py migrate
8) deactivate
9) systemctl start netbox netbox-rq
