print 'Welcome to my Pypet!'

cat = {
  'name': 'Fluffy',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'photo': '(=^o.o^=)__',
  'bored': False,
}

mouse = {
  'name': 'Squeeky',
  'age': 6,
  'weight': 1.5,
  'hungry': False,
  'photo': '<:3 )~~~~',
  'bored': True,
  
}

pets = [cat, mouse]

def feed(pet):
  if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1
    print 'Omnomnomnom! ^-^'
  else:
    print 'The Pypet is not hungry!'

def play(pet):
  if pet['bored'] == True:
    pet['bored'] = False
    print 'You play with ' + pet['name']
  else:
    print 'The Pypet is sleeping. Dont bother it.'

for pet in pets:
  print '______________________________'
  print 'Hello ' + pet['name'] + '!'
  print pet['photo']
  print 'Weight: ' + str(pet['weight'])
  feed (pet)
  print 'Weight: ' + str(pet ['weight'])
  play (pet)
  print '______________________________'
