#!/usr/bin/python
"""
Script for initializing Raspberry servers
It gets auth key from Tailscale API
And runs Ansible playbook
"""

import os
from dotenv import load_dotenv
import requests

def get_auth_key():
    """
    Send request to Tailscale API to generate reusable authentication key 
    which will be used to add new machines to network
    """
    api_token = os.getenv('API_TOKEN')
    tailnet = os.getenv('TAILNET')
    tailscale_url = f'https://api.tailscale.com/api/v2/tailnet/{tailnet}/keys'

    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'capabilities': {
            'devices': {
                'create': {
                    'reusable': True,
                    'ephemeral': False,
                    'preauthorized': False
                }
            }
        },
        'expirySeconds': 300,
        'description': 'Raspberry Pi'
    }
    response = requests.post(url=tailscale_url, headers=headers, json=data, timeout=300)
    return response

# def run_playbook(auth_key):
#     playbook_results = ansible_runner.run(playbook='site.yml')
#     print("{}: {}".format(playbook_results.status, playbook_results.rc))

load_dotenv()
print(get_auth_key().text)
