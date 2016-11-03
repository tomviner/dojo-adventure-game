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



rooms = Bag({
    kitchen,
    library,
    dining_room
})


@when('list rooms')
def list_rooms():
    print("Albermore Manor is a Victorian-era house with:")
    for r in rooms:
        print(r)
