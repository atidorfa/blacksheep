# module 1: different types of assert


def test_a1():
    # only one assert per test scenario
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


def test_a2():
    assert 9 / 5 == 1.5, "failed test intentionally"


def test_a3():
    assert 9 // 5 == 1  # integer division


def test_a4():
    assert 4 != 5


def test_a5():
    assert 1


def test_a6():
    assert ((3 - 1) * 4 / 2) == 4.0


def test_a7():
    assert "put" not in "this is pytest"


def test_a8():
    assert 2 in [1, 2, 4]
    assert [1, 2, 4] == [1, 2, 4]
