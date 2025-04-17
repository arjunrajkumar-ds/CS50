from plates import is_valid, char_limit, special_char, middle_number

def test_char_limit():
    # Checking that plate character length is between [2, 6]
    assert char_limit("A") == False
    assert char_limit("A2") == True
    assert char_limit("QXB073") == True
    assert char_limit("123QWE7") == False

def test_special_char():
    # Checking that no special characters present in string
    assert special_char("QWERTY123") == True
    assert special_char("Hello!") == False
    assert special_char("L33T_") == False
    assert special_char("ME&U") == False

def test_middle_number():
    # Checking that numbers only appear at bookends of plate
    assert middle_number("QW72WW") == False
    assert middle_number("22LAZ3R") == False
    assert middle_number("WENT33") == True

def test_plates():
    assert is_valid("637QQQ") == False
    assert is_valid("QXB073") == False