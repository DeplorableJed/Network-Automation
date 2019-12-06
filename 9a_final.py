import getpass
import sys
import telnetlib

host = "10.X.0.1"
user = input("Enter your telnet username: ")
password = getpass.getpass()

telcon = telnetlib.Telnet(host)

telcon.read_until("Username: ")
telcon.write(user + "\n")
if password:
    telcon.read_until("Password: ")
    telcon.write(password + "\n")

# Change X to your pod number in this section
telcon.write("conf t\n")
telcon.write("int loop 9\n")
telcon.write("ip address 9.9.9.X 255.255.255.255\n")
telcon.write("end\n")
telcon.write("exit\n")

print telcon.read_all()
