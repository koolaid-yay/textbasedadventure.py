#LL AS IL MM Python Final

#Meika Milton v
inventory = [0] # The inventory is a list so that we can have multiple things inside of it and check to see if things are in it.
story_point = 1
#Ian v
rooms = ["outside", 'trap_room']
health = 4

def died(HEALTH):
    HEALTH = 0
    return HEALTH
#adelheiddidthis ^ v
def dead(HEALTH):
        if HEALTH <= 0:
            print("game over press play again to restart")

name = input("before you start your journey, please enter your name here : ") #adelheiddidthis
print("commands n = north w = west e = east s = south i = inventory y = yes n = no") #ian wuz here
print("In a dry desert lays a massive pyramid. Encompassing you in its shadow. Making a cold resting place for weary travelers. \n")
print("a torch lays infront of you  half burried in the sand")
rooms[0]

check = input("do you pick it up : ")

#lucas is silly\/

if check == "y":
    #Meika Milton - added torch
    inventory.append("torch")
    #lucas did this part
    check=input("a door opens in front of you do you enter : ")
else:
    print("nah im too tired i'll come back tomorrow.")
#ian wuz here | Meika making notes here, this code works because we change "check" to be either y or [n] so we can just check it again without having to worry about it still being what they answered before.
if check == 'y':
    print('you find your self in a rather unsuspecting looking room. there is sword in the center of the room')
    check=input('do you pick up the sword : ')
    if check == 'y':
        health-=100
        dead(health)
    else:
        print('now that i think about it that was probably a trap good call') #ian wuz here
    #lucas is sooooooooooooooo weird!!!!!!!!!
        direction=input('now that we missed that trap do you want to go n or w : ')#ian wuz here
        if direction == "n" :
            print("you find yourself in a room that is full of crabs. the crabs eat you and you die.") #adelheiddidthis
            health = died(health)# Meika Milton did the dying code. I wanted to have the two functions that work together and hopefully this works.
            dead(health)
        elif direction == "w": #note from ian who wrote this u need to = signs to make it check to see if its n or w = makes itt n or w
            check=input("You find yourself in a room with a single chest in the center do you open it:")
            if check == "y": 
                check = input("you find a dagger in the chest do you take it:")
                if check == "y":# Meika did the if statement. If they say yes, then we add the dagger to the inventory. Thank you Adelheid!
                    inventory.append("dagger") #adelheiddidthis
            else:
                check=input("i swear to god if you dont take it i will end you, answer wisely:"):
                while check == "n":
                    check=input("")
                    print("")
                
else:
    print("Nah, I'm too tired, I'll come back later or something.")

     





#1 sec im bugging out really bad what did u guys do to my code????? my ifs are gone  ok reload i just did o i see its back yippeee 
 #






#i live... again 1 sec im bugging a lot i may crash 