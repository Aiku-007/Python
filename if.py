pubg_health=int(input("Enter the player'health: "))

if pubg_health>=90:
    print("The health is green.No need to use med.")
elif pubg_health>=50:
    print("The health is yellow. Need to use med.")
else:
    print("Health is critically low and need to use med as soon as possible.")