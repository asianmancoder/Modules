import socket
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = 'utf-8'
ADDRESS = HOST, PORT


def handle_client(conn, addr):
    isConnected = True

    try:
        
        while isConnected:
            data = conn.recv(2048).decode(FORMAT)

            if not data:
                break

            print(f"{addr}: {data}")

    except ConnectionResetError:
        print("The connection has been reset; the client may have disconnected")

        conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(ADDRESS)

    print(f"Server has started, now listening on {PORT} - host is {HOST}")

    server.listen()
    conn, addr = server.accept()
    
    print(f"NEW CONNECTION: {addr}")

    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()

    print(f"THERE ARE {threading.activeCount() - 1} ACTIVE CONNECTIONS")