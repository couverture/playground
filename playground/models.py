from datetime import date


class Person(object):
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    @property
    def age(self):
        age = date.today().year - self.year_of_birth
        return age
