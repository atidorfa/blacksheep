# module 8: fixtures

# fixtures are functions that are run by pytest before (and sometimes after) the actual test functions
# for example: set up DB connection, or initialize webdriver

# can put fixtures inb individual test files, or in conftest.py for making fixtures available in multiple tests

import os

import pytest


@pytest.fixture()
def setup_list():
    # print("...in fixtures..")
    city = ["New York", "London", "Cordoba", "Singapore", "Buenos Aires"]
    return city


def test_get_item(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ["New York", "Cordoba", "Buenos Aires"]


def my_reverse(lst):
    lst.reverse()
    return lst


def test_reverse_list(setup_list):
    assert setup_list[::-2] == ["Buenos Aires", "Cordoba", "New York"]
    assert setup_list[::-1] == my_reverse(setup_list)


@pytest.mark.xfail(
    reason="know issue: usefixture cannot use the fixture's return value"
)
@pytest.mark.usefixtures("setup_list")
def test_usefixture_demo():
    assert 1 == 1
    assert setup_list[0] == "New York"


#############################################################################################


weekdays1 = ["mon", "tue", "wed"]
weekdays2 = ["fri", "sat", "sun"]


@pytest.fixture()
def setup01():
    weekdays1.append("thur")
    yield weekdays1  # yield == return, but it will keep running the function below this line
    print("\n After yield in setup01 fixture")
    weekdays1.pop()


@pytest.fixture()
def setup02():
    weekdays2.insert(0, "thur")
    yield weekdays2  # yield == return, but it will keep running the function below this line
    print("\n After yield in setup02 fixture")


def test_extend_list(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]


def test_len_list(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)


################################################################################################################


filename = "file.txt"


@pytest.fixture()
def setup03():
    f = open(filename, "w")
    f.write("Pytest is awesome")
    f.close()
    f = open(filename, "r+")
    yield f
    f.close()  # will fail if not close
    os.remove(filename)  # delete file from root directory


def test_filetest(setup03):
    assert (setup03.readline()) == "Pytest is awesome"
