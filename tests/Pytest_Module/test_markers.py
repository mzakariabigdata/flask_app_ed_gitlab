import pytest
# marker "-m"
# pytest.exe -v -m "smoke and not strtest" --tb=no
# name (file, function) "-k"
# pytest.exe -v -k str --tb=no
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.zak
def test_str1():
    assert 1 + 2 == 3


def test_str2():
    assert 2 + 2 == 4

@pytest.mark.zak
@pytest.mark.mor
def test_str3():
    assert 1 + 2 == 3