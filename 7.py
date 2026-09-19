import socket

host = "google.com"
port = 443

sock = socket.socket()
sock.settimeout(2)

try:
    sock.connect((host, port))
    print(f"✅ {host}:{port} is UP")
except:
    print(f"❌ {host}:{port} is DOWN")
finally:
    sock.close()