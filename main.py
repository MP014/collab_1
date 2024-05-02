print("Greetings brave adventurer! Please state your name.")
name = input()
print("Well met, " + name + "!")
print("Pick a number between 1 and 4:")
print("1. If you wish to major in IT")
print("2. If you wish to major in science")
print("3. If you wish to major in Engineering")
print("4. If you wish to major in Health Sciences")


attribute = int(input())
character = ""


if attribute == 1:
    character = "cyborg"
    print("Welcome, Cyborg!")
elif attribute == 2:
    character = "Dr. Banner"
    print("Welcome, Incredible Hulk!")
elif attribute == 3:
    character = "Mr. Stark"
    print("Welcome, Iron Man!")
elif attribute == 4:
    character = "Captain"
    print("Welcome, Captain America!")


comms = "As you know, " + character + ", our world has recently been attacked by knowledge zombies."
comms1 = "Knowledge zombies are different from normal zombies in that they eat knowledge instead of brains."
comms3 = "These zombies are extremely dangerous to the people of the world because they feed on "
