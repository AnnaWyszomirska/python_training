# -*- coding: utf-8 -*-
import pytest
import unittest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="grupa lesson1", header="grupa lesson1", footer="grupa lesson1"))
        app.logout()

def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
