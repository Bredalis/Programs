
# Traducir de texto a morce

alfabeto_morce = {
	"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--", " ": " "
}

def traduccion(texto):
	texto = list(texto.lower())

	for i in texto:
		if i in alfabeto_morce.keys():
			print(alfabeto_morce[i], end = "")

traduccion("Hola mi nombre es Bredalis")