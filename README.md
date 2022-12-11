# Morseovka

> Slouží k zakódování nebo dekódování textu do/z morseovky

## Použití

- Možné použít v konzoli, při volání určitých fumkcí

```python
>>> zakodovat("Ahoj")
'.- .... --- .--- '

>>> dekodovat(".- .... --- .---")
'ahoj'
```

- Nebo přímo spuštěním celého skriptu. Například zavoláním morse.py v adresáři

```console
python3 morse.py
```

Skript se nás po zavolání zeptá zda chceme text zakódovat nebo dekódovat.
Poté nás vyzve k vložení nějakého textu k zakódování nebo dekódování.

```console
Tenhle skript slouží k zakódování nebo dekódování morseovky

Zvolte, jestli chcete zakódovat nebo dekódovat text!


1 -> Zakódovat
2 -> Dekódovat
1
Zadejte text, který chcete zakódovat nebo dekódovat:
Ahoj
.- .... --- .--- 
```

Výsledkem nám je zakódovaný, nebo dekódovaný text (string)
```python
'.- .... --- .--- '

'ahoj'
```