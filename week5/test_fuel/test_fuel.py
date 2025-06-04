import pytest
from fuel import convert
from fuel import gauge

def test_valid_fractions():
    assert convert('1/3') == 33
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('0/1') == 0
    assert convert('1/1') == 100
    assert convert('99/100') == 99
    assert convert('1/100') == 1

def test_error_raises():
    with pytest.raises(ValueError):
        convert('3/2')
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('1.5/3')
    with pytest.raises(ZeroDivisionError):
        convert('-1/0')
    with pytest.raises(ValueError):
        convert('1/-2')
    with pytest.raises(ValueError):
        convert('1')
    with pytest.raises(ValueError):
        convert('1/2/3')

def test_gauge_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_gauge_empty():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'

def test_gauge_percentage():
    assert gauge(25) == '25%'
    assert gauge(2) == '2%'
    assert gauge(98) == '98%'