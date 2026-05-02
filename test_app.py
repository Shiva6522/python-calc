from app import add , mul ,divide , sub


def test_add():
    assert add(2,5) == 7
def test_sub():
    assert sub(5,2) == 3
def test_mul():
    assert mul(2,5) == 10
def test_divide():
    assert divide(10/2) == 5
    assert divide(10/0) == 1
