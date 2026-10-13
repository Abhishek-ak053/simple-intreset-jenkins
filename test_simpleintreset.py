from simpleintreset import SimInt

def test_simpleintreset():
    assert SimInt(20000,8,12) == 19200
def test_simpleintreset2():
    assert SimInt(10000,7,0) == 0