print("Greetings brave adventurer! Please state your name.")
Name=input()
print ("Well met "+Name+"!")
print("pick a number between 1 and 4")
print("if you wish to major in IT pick 1")
print("If you wish to major in science pick 2")
print("if you wish to major in Engineering pick 3")
print("If you wish to major in Health Sciences pick 4")
attribute= input()
attribute=int(attribute)
if attribute==1:
     charachter= "cyborg"
     print("Welcome Cyborg!")
elif attribute==2:
          charachter="Dr.Banner"
          print("Welcome Incredible Hulk!")
elif attribute==3:
          charachter= "Mr.Stark"
          print("Welcome Iron Man!")
elif attribute==4:
        charachter= "Capitan"
        print("Welcome Capitan America!")
comms="As you know"+charachter+" our world has recently been attacked by knowlege zombies."
comms1="Knowlage sombies are different from normal zombies in that they eat knowlege instead of brains."
comms3="These zombies are extremely dangerous to the people of the world because they feed on "