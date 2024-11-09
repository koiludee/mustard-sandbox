import pytest

@pytest.fixture()
def pre_post():
    print("Precondition output text")
    yield
    print("\nPostcondition output text")

def test_check_pass():
    assert 1==1

def test_check_failed(pre_post):
    assert 1==2