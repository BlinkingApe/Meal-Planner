#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_meals
----------------------------------

Tests for `meals` module.
"""

import meals


def test_meals_can_instantiate():
    meals_list = [cls for cls in meals.Meal.__subclasses__()]
    for meal in meals_list:
        m = meal()
