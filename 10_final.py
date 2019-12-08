import paramiko
import time

routers = routers = ["10.X.0.1", "10.X.1.2", "10.X.3.3"]
username = "Admin"
password = "NterOne1!"

sshcon = paramiko.SSHClient()
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for target in routers:
    sshcon.connect(hostname=target,username=username,password=password)
    print ("Successful connection", target)
    remote_connection = sshcon.invoke_shell()
    remote_connection.send("configure terminal\n")
    remote_connection.send("int loop 10\n")
    remote_connection.send("ip address 10.0.0.X 255.255.255.255\n")
    remote_connection.send("end\n")
    time.sleep(1)
    output = remote_connection.recv(65535)
    print (output)
    sshcon.close
print("Job completed succesfully")
