# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:16:46 2021

@author: Jenny Xin
"""
import pytest

#a decorator that sets up loop that runs through function multiple times to test diff things
@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (15, "Low")])
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected


@pytest.mark.parametrize("in_string, expected"[
    ("ab", True),
    ("abc", False),
    ("123456", False)])
def test_check_input(in_string, expected):
    from blood_calculator import check_input
    answer = check_input(in_string)
    assert answer == expected