# module 5: marking tests as expected to fail
import sys

import pytest


def test_b1():
    # only one assert per test scenario
    assert 5 + 5 == 10


@pytest.mark.xfail
def test_b2():
    # only one assert per test scenario
    assert 6 + 5 == 10


# @pytest.mark.xfail(reason='known issue')
# @pytest.mark.xfail(raises=TypeError, reason='known issue')
@pytest.mark.xfail(raises=IndexError, reason="known issue")
def test_str04():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[100]


# @pytest.mark.xfail(sys.platform == 'linux', reason="works only in win32")
@pytest.mark.xfail(sys.platform == "win32", reason="works only in win32")
def test_str05():
    letters = "abcd"
    num = 1234
    assert letters + num == "abcd1234"
