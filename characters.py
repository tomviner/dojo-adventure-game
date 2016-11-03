from adventurelib import Item, Bag, when


class Man(Item):
    subject_pronoun = 'he'
    object_pronoun = 'him'


class Woman(Item):
    subject_pronoun = 'she'
    object_pronoun = 'her'


dr_black = the_victim = Man('Dr. Black', 'Dr Black', 'the victim')
dr_black.def_name = 'the victim'
dr_black.description = """\
Dr. Black was the much beloved host and owner of Albermore Manor. His untimely
 death has come as a shock and surprise to most of tonight's guests."""

miss_scarlet = Woman('Miss Scarlet')
miss_scarlet.def_name = 'Miss Scarlet'
miss_scarlet.description = """\
Miss Scarlet is well liked by the younger gentlemen at tonight's gathering.
 She is mistrusted by some and seems to have quite the salacious reputation."""

col_mustard = Man('Colonel Mustard', 'Col. Mustard', 'Col Mustard')
col_mustard.def_name = 'Colonel Mustard'
col_mustard.description = """\
The Colonel is a stern man who accepts no "nonsense". His long and esteemed
 military career has left him with a stiff upper lip and a stiffer drinking
 problem"""

mrs_white = Woman('Mrs. White', 'Mrs White')
mrs_white.def_name = 'Mrs. White'
mrs_white.description = """\
Mrs. White is usually found waiting on the Manor's guests. However tonight she
 has been invited to dine with the others. She seems frazzled and distressed,
 she is nervously glancing around the room.
"""

rev_green = Man(
    'Reverend Green', 'Rev. Green', 'Rev Green', 'Mr. Green', 'Mr Green')
rev_green.def_name = 'Reverend Green'
rev_green.description = """\
Reverend Green is a kindly, wizened old man. Rumour has it that his gambling
 debts make rich men wince.
"""

mrs_peacock = Woman('Mrs. Peacock', 'Mrs Peacock')
mrs_peacock.def_name = 'Mrs. Peacock'
mrs_peacock.description = """\
Mrs. Peacock commands the respect of all she meets. She is the eldest and
 wisest of tonight's guests, her fierce eyes have been known to scare the local
 children.
"""

prof_plum = Man('Professor Plum', 'Prof. Plum', 'Prof Plum')
prof_plum.def_name = 'Professor Plum'
prof_plum.description = """\
Professor Plum is young for a professor, and very ambitious. His latest
 academic paper was widely and loudly critised by the victim.
"""

guests = Bag([
    miss_scarlet, col_mustard, mrs_white, rev_green, mrs_peacock, prof_plum
])


@when('list guests')
def list_guests():
    print("A nearby guest list for tonight's gathering has the following names:")
    for c in guests:
        print(c)


if __name__ == '__main__':
    assert prof_plum == guests.find('Prof. Plum')
    assert prof_plum != guests.find('Plum')
