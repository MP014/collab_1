print("Greetings brave adventurer! Please state your name.")
Name=input()
print ("Well met "+Name+"!")
print ("To get started, log into the EVCC website. Then click on the get started tab and follow the following steps.")
print("To continue through the steps, press enter.")
input()
print("Step 1: determine which educational pathway you'd like to follow")
input()
print("Step 2: Apply for admissions online")
input()
print("Step 3: Find ways to play for college.")
input()
print("Step 4: Complete orientation")
input()
print("Step 5: Establish placement for classes.")
input()
print("Step 6: Complete entry advising and select a pathway.")
input()
print("Step 7: Register and pay for classes")
print ("Before registering for classes, play this quick game to discover recommended classes for your degree")
input()
print("pick a number between 1 and 4")
print("if you wish to major in IT pick 1")
print("If you wish to major in science pick 2")
print("if you wish to major in Engineering pick 3")
print("If you wish to major in Health Sciences pick 4")
attribute= input()
attribute=int(attribute)
if attribute==1:
     charachter= "cyborg"
     print("Charachter chosen: you are Cyborg.")
elif attribute==2:
          charachter="Dr.Banner"
          print("Charachter chosen: you are the Incredible Hulk.")
elif attribute==3:
          charachter= "Mr.Stark"
          print("Charachter chosen: you are Iron Man.")
elif attribute==4:
        charachter= "Capitan"
        print("Charachter chosen: you are Capitan America.")
comms="As you know "+charachter+", our world has recently been attacked by knowledge zombies. "
comms1="Knowledge zombies are very different from normal zombies in that they eat knowledge instead of brains."
comms2="These zombies are extremely dangerous to the people of the world because they are very effective against those without high intellect."
comms3="In order to become an effective fighting force against these zombies, we need you to get smarter"
comms4=" To increase your resistance against their influence, we've developed a training program we call C.O.L.L.E.G.E."
print(comms+comms1+comms2)
input()
print("Don's ask what that stands for, it's so top secret even we don't know.")
input()
print("To activate C.O.L.L.E.G.E. type the command key ENTER on your computer.")
choice=input()
if attribute==1:
     print("Suggested training material:")
     print(" STEM 101, STEM 103, and an English class")
elif attribute==2:
          print("Suggested training material:")
          print("STEM 101, STEM 102, and a Math class")
elif attribute==3:
          print("Suggested training material:")
          print("STEM 101, ENGR 111, and a Math course")
elif attribute==4:
         print("Suggested training material:")
         print("STEM 101, STEM 102, and an English course")
input()
print("Congratulations "+charachter+" You are ready to fight the knowledge zombies!")
print("press enter to attack")
input()
print("BANG BANG BANG")
print("BANG BANG BANG")
print("BANG BANG BANG")
print("BANG BANG BANG")


print("One more time!")
input()
print("BANG BANG BANG")
print("BANG BANG BANG")
print("BANG BANG BANG")
print("BANG BANG BANG")
print("BANG BANG BANG")
input()
print("Congradulations! You defeated the knowlage zobies with what you learned at C.O.L.L.E.G.E.")
print("Now go and finish registration!")
