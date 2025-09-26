#LL AS IL MM Python Final

#Meika Milton v
inventory = [0]
story_point = 1
#Ian v
rooms = ["outside", 'trap_room']
health = 4

#adelheiddidthis
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
#ian wuz here
if check == 'y':
    print('you find your self in a rather unsuspecting looking room. there is sword in the center of the room')
    check=input('do you pick up the sword : ')
    if check == 'y':
        health-=100
        dead(health)
    else:
        print('now that i think about it that was probably a trap good call')
        direction=input('now that we missed that trap do you want to go n or w : ')
else:
    print("nah im too tired i'll come back tomorrow.")















