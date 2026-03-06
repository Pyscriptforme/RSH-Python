import socket


# CLIENT SCRIPT

HOST = "0.0.0.0" # Add the Servers's ip here (target)
PORT = 4444 # Add the server's port that its listening on (target)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print(f"[+] Connected to {HOST}!")
    while True:
        try:
            try:
                cmd = input(f"{HOST}>:")
            except KeyboardInterrupt:
                print("\nExiting..")
                exit()
            s.sendall(cmd.encode())
            out = s.recv(1024)
            if out == "el":
                print("Empty line")
            print(f"{out.decode()}")
        except Exception as e:
            print(f"Error: {e}")
            exit()
