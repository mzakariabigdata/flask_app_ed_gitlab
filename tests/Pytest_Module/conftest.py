import pytest


@pytest.fixture()
def setup_list():
    print ("\n in fixture ... conf")
    city = ['g','b','f', 'l']
    return city