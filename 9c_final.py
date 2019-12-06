import getpass
import sys
import telnetlib

routers = [10.1.0.1, 10.1.1.2, 10.1.3.3]
user = input("Enter your telnet username: ")
password = getpass.getpass()

for target in routers:
    print ("Opening Telnet to " + target)
    telcon = telnetlib.Telnet(target)
    telcon.read_until("Username: ")
    telcon.write(user + "\n")
    if password:
        telcon.read_until("Password: ")
        telcon.write(password + "\n")
    telcon.write("conf t\n")
    for n in range (5,9):
        telcon.write("int loop " + str(n)"\n")
        telcon.write("ip address " + str(n) + ".0.0." + "X" 255.255.255.255\n")
    telcon.write("end\n")
    telcon.write("exit\n")

    print telcon.read_all()
