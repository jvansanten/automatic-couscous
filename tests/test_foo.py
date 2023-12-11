import os

def test_foo():
    """The world's worst test"""
    assert os.uname().sysname == "Linux"