#lists topic in python fully covered
servers=["web01", "web02", "web03"]
ports=[22,34,2222]
servs=["web01",22,True]
se=[]
ser=list()
print(servers[0])
print(servers[-1])
print(servers[-2])
print(servers[-3])
print(len(servers))


servers.append("web04")
print(servers)
servers.insert(5,"web05")
print(servers)

aiko=["web","web1","web2"]
new_aiko=["web3","web4"]
aiko.extend(new_aiko)
print(aiko)

aiko.remove("web")
print(aiko)