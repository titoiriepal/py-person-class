class Person:
    
    people = {}
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self
        
    def __repr__(self):
        return str(self.__dict__)
    


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife"):
            person_list[people.index(person)].wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_list[people.index(person)].husband = Person.people[person["husband"]]
            
    return person_list

