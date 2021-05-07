import socket


HOST = "192.168.0.193"
PORT = 5050
FORMAT = 'utf-8'
ADDRESS = HOST, PORT


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connexion:
    connexion.connect(ADDRESS)

    isConnected = True

    try: 

        while True:
            to_send = input("Type a message here: ").encode(FORMAT)
            connexion.send(to_send)

    except ConnectionResetError:
        print("The connection has been reset - the server may have closed the connection")

        connexion.close()