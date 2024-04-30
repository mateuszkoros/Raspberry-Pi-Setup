# Raspberry-Pi-Setup
Scripts for initial Raspberry Pi setup for local network. Currently steps include:
- Creation of reusable, short-lived auth key to connect machines to Tailscale network
- System upgrade
- Vim installation
- Installation and configuration of Tailscale

Prerequisites:
- _.env_ file with below variables:
    - TAILNET - name of Tailscale network
    - API_TOKEN - token to connect to Tailscale
- _ansible/hosts.ini_ file with addresses of hosts to include in raspberry group
- _ansible/group_vars/raspberry.yml_ with below variables:
    - ansible_ssh_private_key_file
    - ansible_user

To run the script:
```
ansible-galaxy install -r ansible/requirements.yml
pip install -r requirements.txt # preferably in virtualenv
python initialize_servers.py
```