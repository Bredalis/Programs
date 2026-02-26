
print("ASCII encoder and decoder")


def encode_ascii(text: str) -> str:
    """
    Converts each character in the text to its ASCII value.
    """
    try:
        return " ".join(str(ord(char)) for char in text)
    except Exception as error:
        return f"Unexpected error: {error}"


def decode_ascii(text: str) -> str:
    """
    Converts ASCII numbers back into characters.
    """
    try:
        return "".join(chr(int(char)) for char in text.split())
    except Exception as error:
        return f"Unexpected error: {error}"


if __name__ == "__main__":
    sample = "Hello"
    encoded = encode_ascii(sample)
    decoded = decode_ascii(encoded)

    print("Encoded:", encoded)
    print("Decoded:", decoded)
