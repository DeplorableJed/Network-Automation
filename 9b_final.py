import getpass
import sys
import telnetlib
import time

routers = ["10.X.0.1", "10.X.1.2", "10.X.2.3"]
user = input("Enter your telnet username: ")
password = getpass.getpass()
router_id = 1
for target in routers:
    print ("Opening telnet to " + target)
    telcon = telnetlib.Telnet(target)
    telcon.read_until(b"Username: ")
    telcon.write(user.encode("ascii") + b"\n")
    if password:
        telcon.read_until(b"Password: ")
        telcon.write(password.encode("ascii") + b"\n")
    telcon.write(b"conf t\n")
    telcon.write(b"int loop 9\n")
    set_address = "ip address 9.0." + str(router_id) + ".X 255.255.255.255\n"
    telcon.write(bytes(set_address, "ascii"))
    telcon.write(b"end\n")
    telcon.write(b"exit\n")
    router_id = router_id + 1
    time.sleep(0.5)
    print (telcon.read_all().decode("ascii"))
