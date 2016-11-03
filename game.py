import random

people = '123456'
room = 'abcdef'

# murder configuration
#  who was where
#  who is the murderer

# current configuration
#  who was where
#  player location

murder_config_people = list(people)
random.shuffle(murder_config_people)
murder_location = random.choice(room)
murderer = people[room.find(murder_location)]


current_config_people = list(people)
random.shuffle(current_config_people)
current_location = random.choice(room)

print( current_config_people)
print( current_location)
