#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_smoke
----------------------------------

smoke tests for `polyglot` module.
"""

import pytest


def test_for_fire():
    """Make sure nothing blows up while importing polyglot"""
    import polyglot

def test_quick_start_language_detection()
    """Test the quickstart language detection example"""
    from polyglot.text import Text, Word
    text = Text("Bonjour, Mesdames.")
    assert text.language.code == "fr"
    assert text.language.name == "French"

if __name__ == "__main__":
    pytest.main(["-v"])
