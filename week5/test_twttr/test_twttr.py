from twttr import shorten

def test_all_cases():
    assert shorten('Hello') == 'Hll'
    assert shorten('POKEMON') == 'PKMN'
    assert shorten('RacEcAR') == 'RccR'
    assert shorten('AbOminaTion') == 'bmnTn'

def test_numbers():
    assert shorten('123') == '123'
    assert shorten('abc12') == 'bc12'
    assert shorten('AbDe778') == 'bD778'

def test_punctuation():
    assert shorten('Jesús') == 'Jsús'
    assert shorten('Paragüero') == 'Prgür'
    assert shorten('Ámame') == 'Ámm'
    assert shorten('one,two,END') == 'n,tw,ND'
    assert shorten('Dragón.') == 'Drgón.'


