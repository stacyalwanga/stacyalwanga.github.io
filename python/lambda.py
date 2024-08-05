people = [
    {"name" : "Harry", "House": "Gryffindore"},
    {"name" : "Cho", "House" : "Ravenclaw"},
    {"name" : "Draco", "House" : "Slytherine"}
]


people.sort(key=lambda person: person["name"])

print(people)