import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('203.0.40.50', 12345))
    server_socket.listen(1)
    print("Server gestartet und hört auf Port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Verbindung von {addr} akzeptiert")

        data = client_socket.recv(1024).decode()
        print(f"Vom Client empfangene Frage: {data}")

        answer = "Das ist die Antwort auf Ihre Frage"
        client_socket.send(answer.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
