#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_basic
----------------------------------

basic tests for `polyglot` module.
"""

import pytest
import polyglot


@pytest.mark.parametrize(
    "text_input,expected_code,expected_name",
    [
        ("Bonjour, Mesdames.", "fr", "French"),
        (
            u"In Großbritannien war Gandhi mit dem westlichen Lebensstil vertraut geworden",
            "fr",
            "French",
        ),
        ("Preprocessing is an essential step.", "en", "English"),
    ],
)
def test_language_detection(text_input, expected_code, expected_name):
    poly_text = polyglot.Text(text_input)
    assert poly_text.language.code == expected_code
    assert poly_text.language.name == expected_lang


if __name__ == "__main__":
    pytest.main(["-vv"])
