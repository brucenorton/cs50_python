students = [
  {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
  {"name": "Cho", "house": "Ravenclaw", "patronus": "Swan"},
  {"name": "Draco", "house": "Slytherin", "patronus": "Snake"},
  {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
  {"name": "Cedric", "house": "Hufflepuff", "patronus": "Dog"},
  {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},

]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" | ")
    #changess