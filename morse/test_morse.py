import pytest
from morse import zakodovat

def test_morse():
    assert zakodovat("Ahoj, tady Marek") == '.- .... --- .--- --..--  / - .- -.. -.--  / -- .- .-. . -.- '
    assert zakodovat("Tohle je morseovka") == "- --- .... .-.. .  / .--- .  / -- --- .-. ... . --- ...- -.- .- "

    with pytest.raises(TypeError):
        zakodovat(int(26-30<24))
    with pytest.raises(TypeError):
        zakodovat(True)