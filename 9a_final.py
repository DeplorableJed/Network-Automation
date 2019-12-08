import getpass
import sys
import telnetlib

host = "10.X.0.1" #replace X with your pod number
user = input("Enter your telnet username: ")
password = getpass.getpass()
telcon = telnetlib.Telnet(host)
telcon.read_until(b"Username: ")
telcon.write(user.encode("ascii") + b"\n")
if password:
    telcon.read_until(b"Password: ")
    telcon.write(password.encode("ascii") + b"\n")
telcon.write(b"conf t\n")
telcon.write(b"int loop 9\n")
telcon.write(b"ip address 9.0.0.1 255.255.255.255\n")
telcon.write(b"end\n")
telcon.write(b"exit\n")

print (telcon.read_all().decode("ascii"))
