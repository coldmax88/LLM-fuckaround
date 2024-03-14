import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('203.0.40.50', 12345))

    question = "Das ist eine Frage vom Client"
    client_socket.send(question.encode())

    data = client_socket.recv(1024).decode()
    print(f"Vom Server empfangene Antwort: {data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
