from bank import value

def test_greeting_different():
    assert value('buenas tardes') == 100
    assert value('oh hell no') == 100

def test_greeting_h():
    assert value('how is it going?') == 20
    assert value('holly molly') == 20

def test_greeting_hello():
    assert value('hello there') == 0
    assert value('hello, handsome') == 0

def test_case_sensitivity():
    assert value('HELLo') == 0
    assert value('HI!') == 20
    assert value('hOw is it going? ') == 20
    assert value('BRO what') == 100
    
