states={
    "Oregon":'OR',
    'Florida':'FL',
    'California':'CA',
    'Newyork':'NY',
    'Michigan':'MI'
}


cities={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'

}

cities['NY']='New York'
cities['OR']='Portland'


print('-'*10)

print('NY states has:',cities['NY'])
print("OR states has:",cities['OR'])


print('-'*10)

print("Michigan's abbreviation is:",states['Michigan'])
print("Florida's abbreviation is:",states['Florida'])


print('-'*10)

print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

print('-'*10)

for states, abbrev in list(states.items()):
 print(f"state {states} and abbreviated is {abbrev}")

 print('-'*10)

for abbrev,cities in list(cities.items()):
  print(f"{abbrev} has cities {cities}") 

print('-'*10)

for state, abbrev in list(states.items()):
  print(f'{state} state is abbreviated  {abbrev}')
  print(f"and has city {cities[abbrev]}")



print('-'*10)


state=states.get('Texas')

if not state:
  print("Sorry if not Texas")

  city=cities.get('TX','Does not exit')
  print(f"The city for the state 'TX' is:{city}")


