# Raspberry-Pi-Setup
Simple Ansible scripts for initial Raspberry Pi setup for local network. Currently steps include:
- System upgrade
- Vim installation
- Installation and configuration of Tailscale

Prerequisites:
- Tailscale auth key pre-generated and stored in TAILSCALE_KEY environment variable

To run the playbook:
```
ansible-galaxy install -r requirements.yml
ansible-playbook site.yml
```