import paramiko
import time

routers = routers = ["10.X.0.1", "10.X.1.2", "10.X.3.3"]
username = "Admin"
password = "NterOne1!"

sshcon = paramiko.SSHClient()
sshcon.setmissinghostkeypolicy(paramiko.AutoAddPolicy())
for target in routers:
    sshcon.connect(hostname=target,username=username,password=password)
    print ("Successful connection", target)
    remoteconnection = sshcon.invokeshell()
    remote_connection.send("configure terminal\n")
    remote_connection.send("line vty 0 4\n")
    remote_connection.send("transport input all\n")
    remote_connection.send("exit\n")
    remote_connection.send("exit\n")
    remote_connection.send("copy run start\n")
    time.sleep(1)
    output = remote_connection.recv(65535)
    print (output)
    sshcon.close
print("Job completed succesfully")
