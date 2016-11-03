from adventurelib import Item, Bag, when

kitchen = Item('kitchen')
kitchen.description = """\
The kitchen is lined with copper pots and pans.
There is a faint smell of the pea and ham soup that was served at
lunchtime.
"""

library = Item('library')
library.description = """\
The library is panelled with oak and has an impressive collection of
literature and legal tomes.

A copy of the recently-released The Great Gatsby lies on a wooden lamp
table beside a wing chair.
"""

dining_room = Item('dining room', 'dining')
dining_room.description = """\
The imposing dining table is dressed in white linen with a woven golden
border. Silver cutlery is laid in 7 places for dinner... though one will not
be joining them.
"""

conservatory = Item('conservatory')
conservatory.description = """\
Through the tall, narrow panels of the conservatory's glass, you can see that
it is now dark. Any warmth this winter day had has bled away and it feels
distinctly chilly. However, many of the conservatory's plants are bathed in
the warmth of electric lightbulbs.
"""

hall = Item('hall')
hall.description = """\
The hall is a long, bare room, with a marble floor and impressive staircase
carpeted in red. A long table punctuates the centre of the room, and holds
an elaborate spray of white lilies.
"""

study = Item('study')
study.description = """\n
The study's dark oak desk is strewn with paperwork, mostly letters.

A fire burns dimly on the west wall. Beside it, an untouched glass of sherry
awaits a man who will never again drink it.
"""


rooms = Bag({
    kitchen,
    library,
    dining_room,
    conservatory,
    hall,
    study
})


@when('list rooms')
def list_rooms():
    print("Albermore Manor is a Victorian-era house with:")
    for r in rooms:
        print('A', r)
