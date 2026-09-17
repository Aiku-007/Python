filename = "backup.tar.gz"

if filename.endswith((".zip","tar.gz",".gz")):
    print("Compressed file")


url="https://api.example.com"

if url.startswith("https://"):
    print("Secure URL")

log="ERORR ERROR INFO ERROR"
print(log.count("ERROR"))

environment="PRODUCTION"
environment=environment.lower()
if environment=="production":
    print("production environment")

status="running"
print(status.upper())

text="hello world"
print(text.title())
print(text.capitalize())

port="8080"
print(port.isdigit())

port1="8080a"
print(port1.isdigit())

name="Python"
print(name.isalpha())

name1="Python3"
print(name1.isalpha())

value="server123"
print(value.isalnum)

text="  "
print(text.isspace())

server="web01:8080"
parts=server.split(":")
print(parts)

parts1=server.partition(":")
print(parts1)

logs2="""INFO Server started
Warning memory high
ERROR Database failed"""

lines=logs2.splitlines()
print(lines)