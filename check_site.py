import http.client
import socket

site = input("Site: ")

def pingSite(siteName):
    try:
        a = http.client.HTTPConnection(siteName)
        print("Connected to " + siteName)
        a.connect()
    except http.client.http.client.HTTPException as ex:
        print("Not Connected")


def checkPort(siteName):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(siteName, 80)

    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")
    socket.close(result)

pingSite(site)
checkPort(site)
