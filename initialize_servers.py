#!/usr/bin/python
"""
Script for initializing Raspberry servers
It gets auth key from Tailscale API
And runs Ansible playbook
"""

import os
import json
import requests
import ansible_runner
from dotenv import load_dotenv
from datetime import datetime

def get_authentication_key():
    '''
    Send request to Tailscale API to generate reusable authentication key
    which will be used to add new machines to network
    '''
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
    log('Getting authentication key from Tailscale')
    response = requests.post(url=tailscale_url, headers=headers, json=data, timeout=300)
    return json.loads(response.text)['key']

def run_playbook(auth_key):
    '''
    Run Ansible playbook passing received authentication key
    '''
    log('Running Ansible playbook')
    playbook_results = ansible_runner.run(
        private_data_dir='./ansible',
        playbook='site.yml',
        extravars={'tailscale_key': auth_key})
    print(f'{playbook_results.status}: {playbook_results.rc}')

def log(msg):
    '''
    Print message with timestamp
    '''
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'{current_time}: {msg}')


if __name__ == '__main__':
    load_dotenv()
    authentication_key = get_authentication_key()
    run_playbook(authentication_key)
