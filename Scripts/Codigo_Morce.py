
<<<<<<< HEAD
# Pasar de texto a morce
=======
# Traducir de texto a morce

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
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
<<<<<<< HEAD
    return " ".join([alfabeto_morse[i] for i in texto if i in alfabeto_morse.keys()])
=======
    texto_morce = []
    
    for i in texto:
        if i in alfabeto_morse.keys():
            texto_morce.append(alfabeto_morse[i])

    return " ".join(texto_morce)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
