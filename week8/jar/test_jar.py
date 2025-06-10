from jar import Jar
import pytest

def test_create_jar():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    jar = Jar(1)
    assert jar.capacity == 1
    assert jar.size == 0
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_print_cookies():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit_cookies():
    jar = Jar(9)
    with pytest.raises(ValueError):
        jar.deposit(10)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(6)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw_cookies():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)
    jar.withdraw(3)
    assert jar.size == 0