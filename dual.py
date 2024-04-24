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
     print("Welcome Cyborg!")
else:
     if attribute==2:
          print("Welcome Incredible Hulk!")