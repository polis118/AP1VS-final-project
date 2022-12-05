"""@file morse.py.

@brief Prekladac morseovi abecedy.
@author Matulik, Mede, Knapkova, Olexa.
"""

"""Hlavní skript.

Skript slouží ke kódování textu do morseovi abecedy
a zase zpět. Po spuštění se vás skript zeptá,
zda chcete text zakódovat nebo dekódovat.

Po zadání skript vypíše zakódovaný nebo dek'dovaný kód.

Ke spuštění je nutné mít python 3.10 nebo vyšší.
"""
# slovnik s morseovou abecedou
dictMorseovka = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
    "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "ch": "----", "i": "..", "j": ".---", "k": "-.-",
    "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
    "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..", "0": "-----",
    "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ",": "--..--"
}


def zakodovat(text):
    """Tahle funkce slouží k zakodovani.

    Tahle funkce pomocí cyklu vybírá ze stringu
    jedno písmenko po druhém a hledá jej ve slovníku.

    Pokud se v cyklu narazí na mezeru mezi slovy,
    tak se zde vloží znak "/"

    Je jedno, zda při zadávání vložíte velká nebo malá písmena.
    Vždy se velká písmena převádí na malá.

    :param text: (string)

    Sample usage:
    >>> zakodovat("Ahoj")
    '.- .... --- .--- '

    >>> zakodovat("Ahoj svete")
    '.- .... --- .--- / ... ...- . - . '
    """
    if type(text) not in [str]:
        raise TypeError("Value must be string")
    morse = ""
    for char in text:
        if char != " ":
            morse = morse + dictMorseovka.get(char.lower()) + " "
        elif char == " ":
            morse += "/ "
    return morse


def dekodovat(morse):
    """Tahle funkce slouží k dekodovani.

    Tahle funkce slouží k dekódování morseovky na text.
    Uživatel zadává zakódovaný text v morseově abecedě.

    Tahle funkce si rozdělí slovník na "keys" a "values".
    Poté se snaží rozdělit text na jednotlivá slova.
    To pozná podle dělícího znaku "/"

    Dále se zde nachází cyklus pro rozdělení na jednotlivá písmena
    (Mezi písmeny v morseově abecedě se nachází mezera)
    Zde se také nachází další cyklus pro překlad z morseovy abecedy.

    Z listu, kde jsou vložena jednotlivá písmena, se postupně vybírají
    a překládají.

    Pokud je mezi slovy mezera, tak zde bude vložena.

    :param text: (string)

    Sample usage:
    >>> dekodovat(".- .... --- .---")
    'ahoj'

    >>> dekodovat(".- .... --- .--- / ... ...- . - .")
    'ahoj svete'
    """
    if type(morse) not in [str]:
        raise TypeError("Value must be string")
    text = ""
    key_list = list(dictMorseovka.keys())
    val_list = list(dictMorseovka.values())
    splited = morse.split(" / ")
    a = False
    for x in splited:
        splited2 = x.split(" ")
        if a is True:
            text += " "
        a = True
        for y in splited2:
            position = val_list.index(y)
            text += (key_list[position])
    return text


def inputText():
    """Funkce k zadani textu.

    Aby bylo možné ihned vyloučit jestli uživatel zadal správnou
    volbu při výběru kódování nebo dekódování, je potřeba žádat uživatele
    o vstupní text později. Aby jsme se vyvyrovali duplicitnímu kódu,
    tak použijeme tuto funkci.
    """
    return input("Zadejte text, který chcete zakódovat nebo dekódovat: \n")

# Hlavni spousteci podminka programu


if __name__ == "__main__":
    """Hlavní spouštěcí podminka.

    Tahle podminka se spusti jako prvni.
    V tehle podmince se nachazi "Match parser".
    Diky tomu si uzivatel muze vybrat, jetli chce text
    zakodovat nebo dekodovat.
    Pokud zvoli jinou moznost, tak se skript ukonci.

    Jednotlivy case vola zvolenou funkci ke kodovani nebo dekodovani.
    Vystupem je zakodovany nebo dekodovany text.
    """
    print("\nTenhle skript slouží k zakódování nebo dekódování morseovky\n")
    print("Zvolte, jestli chcete zakódovat nebo dekódovat text!\n")
    parse = input("\n1 -> Zakódovat\n2 -> Dekódovat\n")

    match parse:
        case "1":
            vystup = zakodovat(inputText())
            print(vystup)
        case "2":
            vystup = dekodovat(inputText())
            print(vystup)
        case other:
            print("Byla zvolena jiná možnost než zakódovat nebo dekódovat.")
            print("Tahle možnost není k dispozici.\n")
            print("Prosím vyberte si z nabízených možností.")
            exit(0)
