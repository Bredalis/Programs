
# Traducir de texto a morce

alfabeto_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", " ": " "
}

def traduccion(texto):
    texto = list(texto.lower())
    texto_morce = []
    
    for i in texto:
        if i in alfabeto_morse.keys():
            texto_morce.append(alfabeto_morse[i])

    return " ".join(texto_morce)