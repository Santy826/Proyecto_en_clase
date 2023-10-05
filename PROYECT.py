#My Proyect CRUD -> CRUD -> Generar, actualizar, eliminar, buscar

clients = 'Luis, Kevin' #Variable of type string

def create_client(client_name): #Function for creat client
    global clients
    if client_name not in clients: # Si no esta el nombre se añade
        _add_comma()
        clients += client_name
    else:
        print("Client already is in the Client\'s list {}".format(client_name))

# Devuelve la lista de los clientes actualizada
def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients += ", "
    
def read_cliente(client_name): #Function for read client
    global clients 
    if client_name in clients:  
        print(f'The name is,{client_name}')
    else:
        print('The name not available')

def update_cliente(client_name,update_name): #Function Update Client
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ",",update_name+",")
    else:
        print("Error103")
    
    
def delete_cliente(client_name): #Function Delete Client
    global clients
    if client_name in clients:
        # Remove the client name and the trailing comma
        clients = clients.replace(client_name + ",", "")
        print(f"Deleted {client_name}")
    else:
        print("Client not found") 


    
def  _get_client_name(): #Function Get Client y permite preguntar por el nombre del cliente 

    return input("Enter your name: ").upper()




def _print_welcome():
    print("WELCOME TO UNIVERSITY DEL VALLE -TULUA")
    print('*' * 100)
    print("What would do you like to do today")
    print("[C]reate Client o user:")
    print("[R]ead Client o user:")
    print("[U]pdate Client o user:")
    print("[D]elete Client o user:")
   
    




if __name__ == '__main__':
    _print_welcome()
    option = input("Type your activity: ").upper()
    if option =='C':
        #client_name = input("Type your name client: ") Este proceso es repetitivo
        client_name = _get_client_name() #Se obtiene el nombre del cliente
        create_client(client_name) # Se envia el nombre del cliente para crear
        list_clients()
    elif option == 'R':
        client_name = _get_client_name()
        read_cliente(client_name)
        list_clients()
    elif option == 'U':
        #client_name = _get_client_name()
        update_name = input("Which is the update client name:")
        update_cliente(update_name)
        print(clients)
    elif option == 'D':
        client_name = _get_client_name()
        delete_cliente(client_name)
        list_clients()
    else:
         print("Invalid command")
