import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))

    print(f"Server has started, now listening on port {PORT} - host is {HOST}")

    server.listen()
    conn, addr = server.accept()

    with conn:
        print(f"New connection: {addr}")

        connected = True

        try:
            while connected:
                data = conn.recv(2048).decode('utf-8')
                print(f"{addr}: {data}")

                if not data:
                    break

                d = input("Type a message here: ").encode('utf-8')
                conn.sendall(d)

        except ConnectionResetError:
            print(f"An error occured, possibly client {addr} disconnected.")

            conn.close()
