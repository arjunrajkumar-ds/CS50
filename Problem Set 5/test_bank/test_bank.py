from bank import value

def test_value():
    assert value("Hello children") == 0
    assert value("h eeeeeeeee") == 20
    assert value("asdasd") == 100