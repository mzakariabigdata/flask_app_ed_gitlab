import pytest

def test_a1():
    assert 5 + 5 == 10

def test_a2():
    assert 5 + 5 == 10, "Hello"

class TestMyStuff():
    def test_type(self):
        assert type(1.3) == float
    
    def test_strs(self):
        assert str.upper('python') == 'PYTHON'