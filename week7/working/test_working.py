import pytest
from working import convert

def test_valid_inputs():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9:33 AM to 12:00 PM') == '09:33 to 12:00'
    assert convert('5 PM to 10:10 AM') == '17:00 to 10:10'
    assert convert('12 PM to 11 AM') == '12:00 to 11:00'
    assert convert('1:15 AM to 5 PM') == '01:15 to 17:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00' 

def test_missing_parts():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('10:00 to 5 PM')
    with pytest.raises(ValueError):
        convert('9:30 AM to 5')

def test_hour_ranges():
    with pytest.raises(ValueError):
        convert('13:00 AM to 12:00 PM')
    with pytest.raises(ValueError):
        convert('9 AM to 12:60 PM')
    with pytest.raises(ValueError):
        convert('11:77 AM to 9:00 PM')

