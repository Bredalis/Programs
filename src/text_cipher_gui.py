
import tkinter as tk


class TextCipher:
    """Simple GUI application to encrypt and decrypt text."""

    def __init__(self, window):
        self.window = window
        self.is_encrypted = False
        self.saved_texts = []

        self.window.title("Text Cipher")
        self.window.geometry("400x180")
        self.window.resizable(False, False)

        # SAFE icon loading (won't break tests)
        try:
            self.window.iconbitmap("../assets/images/python_logo.ico")
        except Exception:
            pass  # Ignore icon errors in testing environment

        tk.Label(
            self.window,
            text="Enter your text:",
            font=("Times", 16, "italic"),
            pady=12
        ).pack()

        self.text_var = tk.StringVar()

        self.entry_text = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=25,
            textvariable=self.text_var
        )
        self.entry_text.pack(pady=25)

        self.button = tk.Button(
            self.window,
            text="Encrypt",
            font=("Times", 12, "italic"),
            cursor="hand2",
            width=10,
            command=self.toggle_cipher
        )
        self.button.place(x=225, y=100)

    def toggle_cipher(self):
        """Encrypts or decrypts the text depending on the current state."""

        if not self.is_encrypted:
            text = self.text_var.get()
            encrypted = len(text) * "*"

            if "*" not in text:
                self.saved_texts.append(text)

            self.text_var.set(encrypted)
            self.button.config(text="Decrypt")

        else:
            if self.saved_texts:
                self.text_var.set(self.saved_texts[-1])

            self.button.config(text="Encrypt")

        self.is_encrypted = not self.is_encrypted


if __name__ == "__main__":
    root = tk.Tk()
    app = TextCipher(root)
    root.mainloop()
