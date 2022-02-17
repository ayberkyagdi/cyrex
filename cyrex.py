import socket 
import sys
from joblib import Parallel,delayed
import csv

open_ports = []

def get_ports(port) : 
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockets.settimeout(1)
    result = sockets.connect_ex((remote_ip,port))
    if result == 0:
        print(f"Port: {port} is open!")
        open_ports.append(port)
    else:
        print(f"Port: {port} is closed!")
        



if len(sys.argv[1:]) == 1:
    remote_ip = sys.argv[1]

else:
    raise Exception("Wrong number of args!")

print(remote_ip)


Parallel(n_jobs=20, backend='threading')(delayed(get_ports)(port) for port in range(1, 65535))

print(f"Open ports : {open_ports}")


header = ["ip", "port"]
with open('open_ports.csv', "w", encoding = "UTF8") as f:

    writer = csv.writer(f)

    writer.writerow(header)
    for port in open_ports:
        addr = [remote_ip, port]
        
        writer.writerow(addr)
