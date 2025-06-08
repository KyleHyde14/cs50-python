from numb3rs import validate 

def test_validate_all_nums():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.357.0.1") == False
    assert validate("192.168.1") == False
    assert validate('123.223.526.0') == False
    assert validate('123.222.1.500') == False

def test_validate_no_nums():
    assert validate('cat') == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("") == False
    assert validate('cat.dog') == False
    