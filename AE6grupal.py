
from operator import index
from models.client import Client
from models.clients import Clients
from services import users
from helpers import inquirer, uuid_generator

def opt_value(value, name = 'opcion'):
    opcion = value[name].lower()
    return opcion


def run():
    clients_db = users.get()
    clients = Clients()
    if clients_db:
        clients.load_data(clients_db)
    opt = ''
    while opt != 'salir':
        opt = opt_value(inquirer.inquirer_menu())
        if opt == 'bodega':
            print(f'Elegiste el menu {opt}')
            
        elif opt == 'clientes':
            opt_clients = opt_value(inquirer.customer_menu())
            if opt_clients == 'agregar cliente':
                client_ = inquirer.add_client()
                client_ = Client(uuid_generator.create(8), client_['name'], client_['last'], client_['age'], client_['pass'])
                clients.add_client(client_.get_client())
                users.post(clients.get_clients())
                print(f'Se agrego un nuevo cliente con los datos: \n {client_.get_client()}')
            elif opt_clients == 'eliminar cliente':
                name_delete = inquirer.list_client_to_delete(clients.get_clients())['clientes']
                item = [client for client in clients.get_clients() if (f"{client['name']} {client['last']}") == name_delete][0]
                index = clients.get_clients().index(item)
                inquirer.confirm()
                clients.remove_client(index)
                users.post(clients.get_clients())
            elif opt_clients == 'mostrar clientes':
                print(clients.get_clients())
        elif opt == 'envio':
            print(f'Elegiste el menu {opt}')
        else:
            print('Nos vemos')
        if opt != 'salir':
            inquirer.pause();


if __name__ == '__main__':
    run()