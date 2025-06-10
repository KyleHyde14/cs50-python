from seasons import Custom_date, make_song

def test_create_date():
    assert Custom_date('2000-01-12').year == 2000
    assert Custom_date('2000-01-12').month == 1
    assert Custom_date('2000-01-12').day == 12

def test_song():
    assert make_song(Custom_date('2024-06-10').minutes_from_today()) == 'Five hundred twenty-five thousand, six hundred minutes'
    