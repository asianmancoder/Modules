import socket


HOST = "192.168.0.193" # Is this safe to post? Let me know. fire#6945
PORT = 5050


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    connected = True

    try:
        while True:
            d = input("Type a message here: ").encode('utf-8')
            client.sendall(d)

            data = client.recv(2048).decode('utf-8')
            print(f"{HOST}: {data}")

    except ConnectionResetError:
        client.close()

    print(f"Recieved: {repr(data)}")
