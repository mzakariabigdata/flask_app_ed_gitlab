import pytest

# pytest.  -v -s .\Pytest_Module\test_fixtures_simples.py

def test_getItem(setup_list):
    assert setup_list[0] == 'g'

