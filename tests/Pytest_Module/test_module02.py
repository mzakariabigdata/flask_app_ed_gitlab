import pytest

def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert 1/0

def test_case02():
    with pytest.raises(AssertionError):
        # assert 1/0
        assert 3>3

class ValueError(Exception):
    pass

def func1():
    raise ValueError('IndexError func1 raised')

# def test_case03():
#     with pytest.raises(Exception) as excinfo:
#         # assert (1,2,3) == (1,6,6)
#         func1()
#     print( str(excinfo))
#     raise str(excinfo.value) == 'IndexError func1 raised'

