class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age



person = Person('Shlomi', 'Ohana', 25)

print(person.name)