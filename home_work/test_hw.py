def test_1():
    assert ('home', 'work') == ('home', 'work')

def test_2():
    assert 'QA' != 'QC'

def test_3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)