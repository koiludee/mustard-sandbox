import pytest

@pytest.fixture()
def condition_output():
    print("\nPrecondition text")
    yield
    print("\nPostcondition text")

def test_check_pass(condition_output):
    assert 1==1

def test_check_failed(condition_output):
    assert 1==2