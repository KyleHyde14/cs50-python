from plates import is_valid

def test_all_valid():
    assert is_valid('CS50') == True
    assert is_valid('HELLO') == True
    assert is_valid('HI') == True
    assert is_valid('AA') == True
    assert is_valid('AB1234') == True
    assert is_valid('AA30') == True 

def test_correct_length():
    assert is_valid('ABCDEF') == True
    assert is_valid('ABC123') == True
    assert is_valid('CS50000') == False
    assert is_valid('MRW1234') == False
    assert is_valid('A') == False
    assert is_valid('') == False

def test_starts_with_letter():
    assert is_valid('1234') == False
    assert is_valid('=NONO') == False
    assert is_valid('XUD33') == True
    assert is_valid('A1BDC') == False

def test_only_alphanum():
    assert is_valid('CS.50') == False
    assert is_valid('CS!50') == False
    assert is_valid('CS 50') == False

def test_first_num_not_zero():
    assert is_valid('CS05') == False
    assert is_valid('AB00') == False
    assert is_valid('XYZ559') == True

def test_nums_carry_over():
    assert is_valid('CS05B') == False
    assert is_valid('AA333') == True
    assert is_valid('DB10XY') == False
    assert is_valid('XYZ559') == True