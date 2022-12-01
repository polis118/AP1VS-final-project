import pytest
from morse import zakodovat, dekodovat

def test_morse():
    assert zakodovat("Ahoj, tady Marek") == '.- .... --- .--- --..-- / - .- -.. -.-- / -- .- .-. . -.- '
    assert zakodovat("Tohle je morseovka") == "- --- .... .-.. . / .--- . / -- --- .-. ... . --- ...- -.- .- "
    assert dekodovat(".- .... --- .--- --..-- / - .- -.. -.-- / -- .- .-. . -.-") == 'ahoj, tady marek'
    assert dekodovat("- --- .... .-.. . / .--- . / -- --- .-. ... . --- ...- -.- .-") == "tohle je morseovka"

    with pytest.raises(TypeError):
        zakodovat(int(26-30<24))
    with pytest.raises(TypeError):
        zakodovat(True)
    with pytest.raises(TypeError):
        dekodovat(int(26-30<24))
    with pytest.raises(TypeError):
        dekodovat(True)