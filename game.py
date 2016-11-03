import random
from characters import guests as people
from adventurelib import when, start
import rooms
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
        exit()
    else:
        if p:
            print ("%s said: 'How could you!'" % p)
        else:
            print ("No one has ever heard of '%s'!" % person)

@when('in the ROOM')
def locate(room):
    r = rooms.rooms.find(room)
    if murder_location == r:
        print("Yes, the murder happpened in %s" % room)
        exit()
    elif r:
        print("No, there was no murder in the %s" % room)
    else:
        print("Never heard of the %s" % room)


@when('describe PERSONORROOM')
def desc(personorroom):
    thing = people.find(personorroom) or rooms.rooms.find(personorroom)
    if thing:
        print(thing.description)


start()
