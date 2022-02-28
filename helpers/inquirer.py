from calendar import c
from email import message
from re import U
from typing import Text
import inquirer

main_questions = [
    inquirer.List('opcion',
        message='Que desea hacer?',
        choices=['Bodega', 'Clientes', 'Envio', 'Salir']
    ),
]

def inquirer_menu():
    print('=================================')
    print('     Seleccione una opcion       ')
    print('=================================')

    return inquirer.prompt(main_questions)

key_input = [inquirer.Text( name = 'pausa', message= 'Presione ENTER para continuar')]

def pause():
    return inquirer.prompt(key_input)


client_questions = [
    inquirer.List('opcion',
        message='Que desea hacer?',
        choices=['Agregar cliente', 'Eliminar cliente', 'Mostrar clientes', 'Atras']
    ),
]

def customer_menu():
    print('=================================')
    print('            Clientes             ')
    print('=================================')

    return inquirer.prompt(client_questions)


new_client = [
    inquirer.Text( name = 'name', message ='Cual es tu nombre?'),
    inquirer.Text( name = 'last', message ='Cual es tu apellido?'),
    inquirer.Password( name = 'pass', message ='Escribe una contrasena'),
    inquirer.Text( name = 'age', message ='Cual es tu edad?'),
    ]

def add_client():
    return inquirer.prompt(new_client)


def list_client_to_delete(clients = []):
    client_to_delete = [inquirer.List('clientes', 
        message = 'Selecciones el cliente a eliminar', 
        choices = list(map(lambda client: f"{client['name']} {client['last']}", clients)))
    ]
    return inquirer.prompt(client_to_delete)

def confirm():
    question = [
        inquirer.Confirm('confirmar',
            message = 'Quieres continuar?'
        )
    ]
    return inquirer.prompt(question)