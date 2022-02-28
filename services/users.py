import json
from helpers import uuid_generator
from utils import request_http
import os

api_users = 'https://randomuser.me/api/?results=4&inc=name,dob,login'

def get():
    if os.path.exists('.\AE6\grupal\db\clients.json'):
        with open('.\AE6\grupal\db\clients.json') as file:
            data = json.load(file)
        return data
    else:
        users = request_http.get(api_users).json()['results']
        clients = [{'id': uuid_generator.create(8),
                    'name': user['name']['first'],
                    'last': user['name']['last'],
                    'passw': user['login']['password'],
                    'age': user['dob']['age']} for user in users ]
        with open('.\AE6\grupal\db\clients.json', 'w') as file:
            json.dump(clients, file, indent=4)
        return clients

def post(clients):
    with open('.\AE6\grupal\db\clients.json', 'w') as file:
            json.dump(clients, file, indent=4)