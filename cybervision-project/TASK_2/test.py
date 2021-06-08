import json
import requests
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import env as config 
from helper_functions import make_secure_api_call

base_url = config.CYBERVISION["base_url"]
my_token = config.CYBERVISION["x-token-id"]

headers = {
    "x-token-id" : my_token
}


def get_components():
    endpoint_url = '/components'
    response = make_secure_api_call(base_url+endpoint_url,headers)
    data = response.json()
    with open('all_components.txt', 'w') as f:
        f.write(json.dumps(data, indent=2)+"\n")
    return data

def get_groups():
    endpoint_url = '/groups'
    response = make_secure_api_call(base_url+endpoint_url,headers)
    data = response.json()
    with open('groups_final.txt', 'w') as f:
        f.write(json.dumps(data, indent=2)+"\n")


def get_single_group():
    endpoint_url = '/groups'
    endpoint_url = endpoint_url + '/41c6fdde-77e4-451e-930b-4d99bd409c40'
    response = requests.get(url=base_url+endpoint_url,headers=headers, verify=False)
    data = response.json()
    with open('single_group.txt', 'w') as f:
        f.write(json.dumps(data, indent=2)+"\n")

def delete_groups():
    gids = []
    with open('group_ids.txt', 'r') as f:
        gids = f.read().split()
    for d in gids:
        endpoint_url = "/groups/" + d
        response = requests.delete(url=base_url+endpoint_url, headers=headers, verify=False)
        print(response.status_code)
    open('group_ids.txt', 'w').close()



