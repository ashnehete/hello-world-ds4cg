from cdstemplate.hello_world import hello


def test_hello_world():
    assert hello() == "Hello, World!"


def test_hello_name():
    assert hello("Aashish") == "Hello, Aashish!"
