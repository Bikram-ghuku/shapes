import pytest
import main

def test_rectrangle_perimeter():
    assert main.rectangle.perimeter == 68.0, "test failed"

def test_rectangle_area():
    assert main.rectangle.area == 288.0, "test failed"

def test_square_area():
    assert main.square.area == 4.0, "test failed"

def test_square_perimeter():
    assert main.square.perimeter == 8.0, "test failed"

