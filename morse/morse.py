"""Hlavní skript.

Zde bude hlavni skript celeho projektu.
"""
# slovnik s morseovou abecedou
dictMorseovka = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "ch": "----", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}


def zakodovat(text):
    """Tahle funkce slouží k zakodovani.
    
    Text k funkci.
    """

    return text


def dekodovat(text):
    """Tahle funkce slouží k dekodovani.
    
    Text k funkci.
    """

    return text

def inputText():
    """Funkce k zadani textu.
    
    Aby bylo možné ihned vyloučit jestli uživatel zadal správnou volbu při výběru kódování nebo dekódování, je potřeba žádat uživatele
    o v stupní text později. Aby jsme se vyvyrovali duplicitnímu kódu, tak použijeme tuto funkci.
    """

    return input("Zadejte text, který chcete zakódovat nebo dekódovat: \n----------------------------------------------------\n")

if __name__ == "__main__":
    """Hlavní spouštěcí podminka.

    Tahle podminka se spusti jako prvni.
    V tehle podmince se nachazi "Match parser".
    Diky tomu si uzivatel muze vybrat, jetli chce text zakodovat nebo dekodovat.
    Pokud zvoli jinou moznost, tak se skript ukonci.

    Jednotlivy case vola zvolenou funkci ke kodovani nebo dekodovani.
    Vystupem je zakodovany nebo dekodovany text.
    """

    print("Tenhle skript slouží k zakódování nebo dekódování morseovky\n")
    print("Zvolte, jestli chcete zakódovat nebo dekódovat text!\n----------------------------------------------------\n")
    parse = input("1 -> Zakódovat\n2 -> Dekódovat\n")

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