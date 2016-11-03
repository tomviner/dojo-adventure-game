import random
from adventurelib import Item, Bag, when, start
import rooms
import characters
from sys import exit


people = '123456'
rooms = 'abcdef'

# murder configuration
#  who was where
#  who is the murderer

# current configuration
#  who was where
#  player location

murder_config_people = list(people)
random.shuffle(murder_config_people)
murder_location = random.choice(rooms)
murderer = people[rooms.find(murder_location)]


current_config_people = list(people)
random.shuffle(current_config_people)
current_location = random.choice(rooms)

@when('where am i')
def my_room():
    print("I am in: ", current_location)

@when('go to ROOM')
@when('go to the ROOM')
def to_room(room):
    if room in rooms:
        print("I am now in %s" % room)
        global current_location
        current_location = room
    else:
        print("I can't find the %s" % room)

@when('it was M')
def accuse(m):
    if m == murderer:
        print ("Yes, %s is the murderer!" % m)
        exit
    else:
        if m in people:
            print ("%s said: 'How could you!'" % m)
        else:
            print ("No one has ever heard of '%s'!" % m)


start()
