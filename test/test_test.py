import pytest

@pytest.fixture()
def pre_post():
    print("Precondition output text")
    yield
    print("\nPostcondition output text")

def test_check_pass(pre_post):
    assert 1==1
