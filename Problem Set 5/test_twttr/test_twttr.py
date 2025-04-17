from twttr import shorten

def test_shorten():
    assert shorten('Arjun') == 'rjn'
    assert shorten('zyn') == 'zyn'
    assert shorten('banana') == 'bnn'
    assert shorten('637Arjun343') == 'rjn'