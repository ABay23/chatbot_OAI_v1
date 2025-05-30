
def test_equal_or_not():
    assert 3 == 3
    
def test_equal_or_not2():
    assert 3 == 3
    
def test_differences():
    assert 'action' == 'action'
    
def test_one_differences():
    assert 'action' == 'action'
    
def test_string_validation():
    assert isinstance('this is a string', str)
    
def test_boolean():
    values = True
    assert values is True