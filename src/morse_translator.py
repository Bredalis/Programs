
# Convert text to Morse code

MORSE_ALPHABET = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", " ": " "
}


def translate_to_morse(text: str) -> str:
    """
    Translates plain text into Morse code.
    """
    text = text.lower()
    return " ".join(
        MORSE_ALPHABET[char]
        for char in text
        if char in MORSE_ALPHABET
    )


if __name__ == "__main__":
    sample_text = "hello world"
    print(translate_to_morse(sample_text))
