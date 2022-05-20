from main import read_root


def test_root():
    assert read_root() == {"Hello": "Hello World from VCP"}
