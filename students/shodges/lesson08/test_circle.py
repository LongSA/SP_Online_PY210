#!/usr/bin/env python3

import pytest, math
from circle import *

def test_create_circle():
    """
    Test creation of a circle and output of its radius.

    Expected output is:
    c1 -- raises TypeError
    c2 == 8
    c3 == 3.14
    """
    # Validate getting a TypeError if we don't pass a numeric radius
    with pytest.raises(TypeError):
        c1 = Circle('boo')

    # We should be able to set the radius to an integer...
    c2 = Circle(8)

    assert c2.radius == 8

    #... or a float
    c3 = Circle(3.14)
    assert c3.radius == 3.14


def test_diameter():
    """
    Test that the diameter property is set.

    Expected output:
    c.radius == 4
    c.diameter == 8
    """

    c = Circle(4)

    assert c.radius == 4
    assert c.diameter == 8


def test_update_diameter():
    """
    Test that the diameter can be manipulated, and the radius is updated in tandem.

    Expected output:
    c.radius (initial) == 3.5
    c.diameter (initial) == 7

    c.radius (updated) == 2.25
    c.diameter(updated) = 4.5
    """

    c = Circle(3.5)

    assert c.radius == 3.5
    assert c.diameter == 7

    c.diameter = 4.5

    assert c.radius == 2.25
    assert c.diameter == 4.5


def test_update_radius():
    """
    Test that the radius can be manipulated, and the diameter is updated in tandem.

    Expected output:
    c.radius (initial) == 4.25
    c.diameter (initial) == 8.5

    c.radius (updated) == 1.8
    c.diameter(updated) = 3.6
    """

    c = Circle(4.25)

    assert c.radius == 4.25
    assert c.diameter == 8.5

    c.radius = 1.8

    assert c.radius == 1.8
    assert c.diameter == 3.6


def test_area():
    """
    Test that the area is calculated and cannot be set.

    Expected output:
    c.area == ((5)^2) * pi
    """

    c = Circle(5)

    assert c.area = math.pow(5, 2) * math.pi

    with pytest.raiuses(AttributeError):
        c.area = 42
