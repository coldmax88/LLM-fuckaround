import socket
serverip="34.116.232.56"
Port=12345
def start_client():
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((serverip, Port))
    
        question = str(input("Nutzer:    "))
        client_socket.send(question.encode())
    
        data = client_socket.recv(1024).decode()
        print(f"KI:    {data}")
    
        client_socket.close()

if __name__ == "__main__":
    start_client()
