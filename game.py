import random
from characters import guests, butler
from adventurelib import when, start, Bag
from rooms import rooms
from sys import exit


def set_up_murder():
    global murderer, murder_location

    # Initialise rooms
    for r in rooms:
        r.people = Bag()
        r.at_the_time_of_the_murder = Bag()

    murder_locations = Bag(rooms)
    murder_config_guests = Bag(guests)

    # Select a murderer and place them into a room on their own
    murderer = murder_config_guests.take_random()
    murder_location = murder_locations.take_random()
    murder_location.at_the_time_of_the_murder.add(murderer)
    # The murderer will lie about where he/she was
    murderer.at_the_time_of_the_murder = rooms.get_random()

    # Randomly place the other guests into the other rooms at the time of
    # the murder
    for p in murder_config_guests:
        location = murder_locations.get_random()
        location.at_the_time_of_the_murder.add(p)
        p.at_the_time_of_the_murder = location

    rooms_now = Bag(rooms)
    # Put the butler into the hall
    rooms_now.take('hall').people.add(butler)
    # Place everyone at random into their rooms now
    for p in guests:
        rooms_now.get_random().people.add(p)


set_up_murder()
current_location = rooms.find('hall')


@when('where am i')
def my_room():
    print("You are in the", current_location)


@when('go to ROOM')
@when('go to the ROOM')
def to_room(room):
    global current_location
    r = rooms.find(room)
    if current_location == r:
        print("You are already in %s." % room)
    elif r:
        current_location = r
        look()


def format_people(people):
    people = list(people)
    if len(people) > 1:
        return '%s and %s' % (
            ', '.join(str(p) for p in people[:-1]),
            people[-1]
        )
    else:
        return str(people[0])


@when('look')
def look():
    print(current_location.description)
    people_here = current_location.people
    if len(people_here) > 1:
        print(format_people(people_here), 'are here.')
    elif len(people_here) == 1:
        print(format_people(people_here), 'is here.')


@when('look at GUEST')
def look_at(guest):
    g = current_location.people.find(guest)
    if g:
        print(g.description)
    else:
        print("%s is not here." % guest.title())


@when('talk to GUEST')
def talk_to(guest):
    g = current_location.people.find(guest)
    if g is butler:
        print('''"You saw me in the King's Arms yourself at the time of the
        murder, inspector!", he reminds you.

        "You saw me dash out when I took the call!"''')
    elif g:
        if g is murderer:
            # The murderer will claim he/she was alone
            people_near = set()
        else:
            people_near = Bag(g.at_the_time_of_the_murder.at_the_time_of_the_murder)
            people_near.discard(g)

        if current_location is g.at_the_time_of_the_murder:
            location = 'here'
        else:
            location = 'in the {}'.format(g.at_the_time_of_the_murder)
        print('"I was {} at the time of the murder{}," {} says.'.format(
            location,
            ', with %s' % format_people(people_near) if people_near else '',
            g.subject_pronoun
        ))
        other_rooms = Bag(rooms)
        other_rooms.discard(current_location)
        next_room = other_rooms.get_random()
        current_location.people.remove(g)
        next_room.people.add(g)

        print()
        print('{} wanders off in the direction of the {}.'.format(
            g.subject_pronoun.title(),
            next_room
        ))
    else:
        print("%s is not here." % guest.title())


@when('it was PERSON')
def accuse(person):
    p = guests.find(person)
    if p == murderer:
        print ("Yes, %s is the murderer!" % p)
        exit()
    else:
        if p:
            print ("%s said: 'How could you!'" % p)
        else:
            print ("No one has ever heard of '%s'!" % person)


print("""\
"Welcome to Albermore Manor, Inspector.", says the butler as he lets you in.
"I'm sorry you're here under such dark circumstances."

"The guests tell me they heard Dr. Black scream at around 7:30pm, and found
him dead in the {}."
""".format(murder_location))

start()
