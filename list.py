# list
cities =["Nagpur","pune","Indore","Bhopal"]

print('third position in list = {}'.format(cities[2]))

print(cities)

# Append in a list
cities.append("chhindwara")
print('appended list = {}'.format(cities))

# inserting at choosen position
cities.insert(3,"Shrinagar")
print('inserted value in a list  = {}'.format(cities))

# deleting element from list

cities.pop()
print('list after pop operation  = {}'.format(cities))

# printing the values of list using for loop
print('List of cities')
for city in cities:
    print(city)
countries =["USA","South Korea","India","Japan"]
print('List of countries')
for country in countries:
    print(country)
