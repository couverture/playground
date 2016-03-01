def test_person():
    from playground.models import Person
    person = Person("muzzy", 1980)


def test_person_age():
    from playground.models import Person
    person = Person("muzzy", 1980)
    assert person.age == 36


def test_person_upper_name():
    from plauground.models import Person
    person = Person("muzzy", 1980)
    assert person.upper_name() == 'MUZZY'
