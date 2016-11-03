import random
from characters import guests as people
from adventurelib import Item, Bag, when, start
import rooms
import characters
from sys import exit



murder_config_people = list(people)
random.shuffle(murder_config_people)
murder_location = random.choice(list(rooms.rooms))
murderer = random.choice(list(people))


current_config_people = list(people)
random.shuffle(current_config_people)
current_location = random.choice(list(rooms.rooms))

@when('where am i')
def my_room():
    print("I am in: ", current_location)

@when('go to ROOM')
@when('go to the ROOM')
def to_room(room):
    global current_location
    r = rooms.rooms.find(room)
    if current_location == r:
        print("I am already in %s" % room)
    elif r:
        print("I am now in %s" % room)
        current_location = r
    else:
        print("I can't find the %s" % room)

@when('it was PERSON')
def accuse(person):
    p = people.find(person)
    if p == murderer:
        print ("Yes, %s is the murderer!" % p)
        exit
    else:
        if p:
            print ("%s said: 'How could you!'" % p)
        else:
            print ("No one has ever heard of '%s'!" % person)


start()
