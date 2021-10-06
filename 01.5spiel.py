import random
import time


range = pirat=random.randint(1,100)


print("Hallo ich bin Käptn Hook und habe mir eine zahl ausgedacht, wenn du sie errätst, bekommst du deine Beute! du hast 6 Versuche.")
time.sleep(0.5)
Zahl=int(input("Errate die Zahl zwischen 1-100"))


if pirat==Zahl:
    print("DU HAST DIE BEUTE ERLANGT!!\n ")
    exit()


if Zahl < pirat:
    print("Zu niedrig, du Landratte! !")
else: print("zu hoch .")


Zahl=int(input("noch 5 Versuche!\n"))
if pirat==Zahl:
    print("DU HAST DIE BEUTE ERLANGT!!\n ")
    exit()


if Zahl < pirat:
    print("Zu niedrig, du Landratte!!")
else: print("zu hoch.")


Zahl=int(input("noch 4 Versuche!\n"))
if pirat==Zahl:
    print("DU HAST DIE BEUTE ERLANGT!\n")
    exit()


if Zahl < pirat:
    print("Zu niedrig, du Landratte!!")
else: print("zu hoch .")


Zahl=int(input("noch 3 Versuche\n!"))
if pirat==Zahl:
    print("DU HAST DIE BEUTE ERLANGT!\n")
    exit()


if Zahl < pirat:
    print("Zu niedrig, du Landratte!")
else: print("zu hoch .")
Zahl=int(input("noch 2 Versuche Kamerad!\n"))

               
if pirat==Zahl:
    print("DU HAST DIE BEUTE ERLANGT!\n")
    exit()


if Zahl < pirat:
    print("Zu niedrig, du Landratte!!\n")
else: print("zu hoch.")
Zahl=int(input("noch 1 Versuch !"))


if pirat==Zahl:
    print("DU HAST DIE BEUTE ERLANGT!\n")
    exit()


if Zahl < pirat:
    print("Zu niedrig, du Landratte!")

    
else: print("zu hoch.")
print("Game over")
exit()
