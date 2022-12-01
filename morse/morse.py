"""Hlavní skript.

Zde bude hlavni skript celeho projektu.

Ke spuštění je nutné mít python 3.10 nebo vyšší. 
"""
# slovnik s morseovou abecedou
dictMorseovka = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "ch": "----", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ",": "--..--"
}


def zakodovat(text):
    """Tahle funkce slouží k zakodovani.

    Text k funkci.
    """
    morse = ""
    for char in text:
        if char != " ":
            morse = morse + dictMorseovka.get(char.lower()) + " "
        elif char == " ":
            morse += "/ "
    return morse


def dekodovat(morse):
    """Tahle funkce slouží k dekodovani.
    
    Text k funkci.
    """

    text=""
    key_list = list(dictMorseovka.keys())
    val_list = list(dictMorseovka.values())
    splited = morse.split(" / ")
    print(splited)
    a = False
    for x in splited:
        splited2 = x.split(" ")
        if a is True:
            text += " "
        a = True
        for y in splited2:
            print(y)
            position = val_list.index(y)
            text += (key_list[position])
    return text


def inputText():
    """Funkce k zadani textu.
    
    Aby bylo možné ihned vyloučit jestli uživatel zadal správnou volbu při výběru kódování nebo dekódování, je potřeba žádat uživatele
    o v stupní text později. Aby jsme se vyvyrovali duplicitnímu kódu, tak použijeme tuto funkci.
    """

    return input("Zadejte text, který chcete zakódovat nebo dekódovat: \n----------------------------------------------------\n")

# Hlavni spousteci podminka programu
if __name__ == "__main__":
    """Hlavní spouštěcí podminka.

    Tahle podminka se spusti jako prvni.
    V tehle podmince se nachazi "Match parser".
    Diky tomu si uzivatel muze vybrat, jetli chce text zakodovat nebo dekodovat.
    Pokud zvoli jinou moznost, tak se skript ukonci.

    Jednotlivy case vola zvolenou funkci ke kodovani nebo dekodovani.
    Vystupem je zakodovany nebo dekodovany text.
    """

    print("\nTenhle skript slouží k zakódování nebo dekódování morseovky\n")
    parse = input("Zvolte, jestli chcete zakódovat nebo dekódovat text!\n----------------------------------------------------\n1 -> Zakódovat\n2 -> Dekódovat\n")

    match parse:
        case "1":
            vystup = zakodovat(inputText())
            print(vystup)
        case "2":
            vystup = dekodovat(inputText())
            print(vystup)
        case other:
            print("Byla zvolena jiná možnost než zakódovat nebo dekódovat. Tahle možnost není k dispozici.\n Prosím vyberte si z nabízených možností.")
            exit(0)