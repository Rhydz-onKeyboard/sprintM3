import inquirer


def inquirer_menu():
    print('=================================')
    print('     Seleccione una opcion       ')
    print('=================================')

    main_questions = [
        inquirer.List('opcion',
            message='Que desea hacer?',
            choices=['Bodega', 'Clientes', 'Envio', 'Salir']
        ),
    ]

    return inquirer.prompt(main_questions)


def pause():
    key_input = [inquirer.Text( name = 'pausa', message= 'Presione ENTER para continuar')]
    return inquirer.prompt(key_input)



def customer_menu():
    print('=================================')
    print('            Clientes             ')
    print('=================================')
  
    client_questions = [
        inquirer.List('opcion',
            message='Que desea hacer?',
            choices=['Agregar cliente', 'Eliminar cliente', 'Mostrar clientes', 'Atras']
        ),
    ]

    return inquirer.prompt(client_questions)



def add_client():
    new_client = [
        inquirer.Text( name = 'name', message ='Cual es tu nombre?'),
        inquirer.Text( name = 'last', message ='Cual es tu apellido?'),
        inquirer.Password( name = 'pass', message ='Escribe una contrasena'),
        inquirer.Text( name = 'age', message ='Cual es tu edad?'),
        ]
    return inquirer.prompt(new_client)


def list_client_to_delete(clients = []):
    client_to_delete = [inquirer.List('clientes', 
        message = 'Selecciones el cliente a eliminar', 
        choices = list(map(lambda client: f"{client['name']} {client['last']}", clients)))
    ]
    return inquirer.prompt(client_to_delete)

def confirm_remove_client():
    question = [
        inquirer.Confirm('confirmar',
            message = 'Se eliminara el cliente, quieres continuar?'
        )
    ]
    return inquirer.prompt(question)