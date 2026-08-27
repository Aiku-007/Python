text="Devops"
print(text[0])
print(text[::-1])
print(text[1:3:1])
#strings are immutable
word="Python"
modified_word=word.upper()
print(modified_word)
lower_word=word.lower()
print(lower_word)

username="   Aiko Aiko  "
h=username.strip()

print(h)
updated=username.lstrip()
updated_1=username.rstrip()
print(updated)
print(updated_1)

aalu="Python is Powerful"
aalu_1=aalu.find("Python")
aalu_2=aalu.find("aalu")
aalu_3=aalu.count("Python")
print(aalu_1)
print(aalu_2)
print(aalu_3)

name="production-server"
print(name.startswith("production"))
print(name.startswith("productin"))

filename="Server.log"
print(filename.endswith(".log"))

filename_2 = "application.log"

if filename_2.endswith(".log"):
    print("This is a log file")

log= "ERROR: Database connection failed"

if "ERROR" in log:
    print("Alert")

nline="Python is Powerful"
wds=nline.split()
print(wds)

data = "server01,10.0.0.5,running"
parts = data.split(",")
print(parts)

data_1="""Python
Docker
Kuberntes"""
data_5=data_1.splitlines()
print(data_5)

alphas=["Python","is","Powerful"]
sentence=" ".join(alphas)
print(sentence)

logg="ERROR: Database failed"
new_log=logg.replace("ERROR","WARNING")
print(new_log)

we="###hello###"
we_1=we.strip("#")
print(we_1)

print("123".isdigit())
print("123q".isdigit())

print("Python".isalpha())
print("Python5".isalpha())


print("Python3".isalnum())
print("Python 3".isalnum())

print("hello".islower())
print("Hello".islower())

print("   ".isspace())

print("HELLO".isupper())
print("HEllo".isupper())

my_name="Aiko"
age=20

print(f"My name is {my_name} and I am {age}")

cpu=75
print(f"CPU usage: cpu{cpu}%")
a=12
b=34
print(f"total:{a+b}")

price=83.4444
print(f"price={price:.2f}")

print("HEllo\nAiko")
print("HEllo\tAiko")
print("HEllo\\Aiko")
print("He said \"hello\"")

path=r"C:\USers\Aiko\Documents"
print(path)