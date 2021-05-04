import socket


HOST = "192.168.0.193"
PORT = 5050


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    connected = True

    try:
        while True:
            d = bytes(input("Type a message here: "), 'utf-8')
            client.sendall(d)

            data = client.recv(2048)
            print(f"{HOST}: {data}")

    except ConnectionResetError:
        client.close()

    print(f"Recieved: {repr(data)}")