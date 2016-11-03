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
 military career has left him with"""

mrs_white = Woman('Mrs. White', 'Mrs White')
mrs_white.def_name = 'Mrs. White'

rev_green = Man(
    'Reverend Green', 'Rev. Green', 'Rev Green', 'Mr. Green', 'Mr Green')
rev_green.def_name = 'Reverend Green'

mrs_peacock = Woman('Mrs. Peacock', 'Mrs Peacock')
mrs_peacock.def_name = 'Mrs. Peacock'

prof_plum = Man('Professor Plum', 'Prof. Plum', 'Prof Plum')
prof_plum.def_name = 'Prefessor Plum'

guests = Bag([
    miss_scarlet, col_mustard, mrs_white, rev_green, mrs_peacock, prof_plum
])


@when('list guests')
def list_rooms():
    print("A nearby guest list for tonight's gathering has the following names:")
    for c in guests:
        print(c)


if __name__ == '__main__':
    assert prof_plum == guests.find('Prof. Plum')
    assert prof_plum != guests.find('Plum')
