class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def generate_people():
    people = []
    people.append(Person("Alice", 30))
    people.append(Person("Bob", 25))
    people.append(Person("Charlie", 22))
    return people

# Генерация списка объектов
people_list = generate_people()

# Создание словаря с объектами класса и собственными идентификаторами
people_dict = {}
id_counter = 1

for person in people_list:
    people_dict[id_counter] = person
    id_counter += 1

# Вывод информации о объектах в словаре
for key, value in people_dict.items():
    print(f"ID: {key}, Name: {value.name}, Age: {value.age}")