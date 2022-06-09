# Skipping tests

import sys

import pytest

pytestmark = pytest.mark.skipif(
    sys.platform != "win32", reason="will run only in Linux OS"
)
const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


# print(cent_to_fah())


@pytest.mark.skip(reason="skipping for no reason specified")
def test_case01():
    assert type(const) == float


# @pytest.mark.skipif(cent_to_fah() == 32, reason="skipping because default value test")
@pytest.mark.skipif(
    sys.version_info > (3, 6), reason="doesn't work on py version above 3.6"
)
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(
    pytest.__version__ < "7.5.0", reason="doesn't work on pytest version below 7.5.0"
)
def test_case03():
    assert cent_to_fah(38) == 100.4
