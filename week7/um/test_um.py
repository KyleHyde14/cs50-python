from um import count

def test_only_um():
    assert count("um") == 1

def test_um_no_alphanum():
    assert count("  um  ") == 1
    assert count("!um") == 1
    assert count("um, um, um!") == 3

def test_no_um_alone():
    assert count("there is no word to match here") == 0
    assert count('this mummy is from Egypt') == 0
    assert count('YUMMY') == 0

def test_um_in_sentences():
    assert count('um... What was I saying?') == 1
    assert count('UM...OH...UM! I forgot') == 2
    assert count('Hello, um... you...um... yeah you') == 2
    assert count('Yeah Um... um... UM...why is this so hard?') == 3