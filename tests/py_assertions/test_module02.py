import pytest


def raise_value_error():
    raise ValueError("Exception raised")


def test_case01():
    with pytest.raises(Exception):  # expects an exception to poss
        assert 3 > 3


def test_case02():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0


def test_case03():
    with pytest.raises(Exception) as e:
        assert (1, 2, 3) == (1, 2, 4)
    print("\n" + str(e))


def test_case04():
    with pytest.raises(Exception) as e:
        raise_value_error()
    print("\n" + str(e))
    assert (str(e.value)) == "Exception raised"
