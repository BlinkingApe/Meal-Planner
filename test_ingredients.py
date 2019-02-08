#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_meals
----------------------------------

Tests for `meals` module.
"""

import ingredients


def test_meals_can_instantiate():
    ing_list = [cls for cls in ingredients.Ingredient.__subclasses__()]
    for ing in ing_list:
        i = ing(1)
