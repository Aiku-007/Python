server = ("web01", "web02", "web01", "web03", "web01")

print(server.count("web01"))
print(server.index("web03"))

first, *middle, last = server
print(server)