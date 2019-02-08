#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mealplan
----------------------------------

Tests for `mealplan` module.
"""
import mealplan


def test_select_random_meals():
    meals_list = mealplan.select_random_meals(n=3)
    assert len(meals_list) == 3
