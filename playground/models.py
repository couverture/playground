class Person(object):
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    @property
    def age(self):
        return date.today().year - self.year_of_birth
