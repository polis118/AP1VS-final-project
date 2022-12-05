"""Tohle je testovací skript.

Tímhle skriptem se testuje skript morse.py
"""


import pytest
from morse import *


def test_morse():
    """Tohle je testovací funkce.

    Postupně se testuje jestli se text správně zakoduje do morseovky a naopak.
    Poté dochází k testování datových typů.
    """
    morse1 = '.- .... --- .--- --..-- / - .- -.. -.-- / -- .- .-. . -.- '
    morse2 = "- --- .... .-.. . / .--- . / -- --- .-. ... . --- ...- -.- .- "
    morse3 = '.- .... --- .--- --..-- / - .- -.. -.-- / -- .- .-. . -.-'
    morse4 = "- --- .... .-.. . / .--- . / -- --- .-. ... . --- ...- -.- .-"
    text1 = 'ahoj, tady marek'
    text2 = "tohle je morseovka"

    assert zakodovat("Ahoj, tady Marek") == morse1
    assert zakodovat("Tohle je morseovka") == morse2
    assert dekodovat(morse3) == text1
    assert dekodovat(morse4) == text2

    with pytest.raises(TypeError):
        zakodovat(int(26 - 30 < 24))
    with pytest.raises(TypeError):
        zakodovat(True)
    with pytest.raises(TypeError):
        dekodovat(int(26 - 30 < 24))
    with pytest.raises(TypeError):
        dekodovat(True)
