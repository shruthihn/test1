import pytest


def test_m1():
    print("changes done")


def test_m2():
    print("changed")


def test_m3():
    pass


def test_m4():
    e_r='abc logged in'
    a_r='abc logged in'
    assert e_r==a_r
