
from path_setup import *

import unittest
import tkinter as tk
from text_cipher_gui import TextCipher


class TestTextCipher(unittest.TestCase):
    """Unit tests for the TextCipher GUI application."""

    def setUp(self):
        self.window = tk.Tk()
        self.app = TextCipher(self.window)

    def tearDown(self):
        self.window.destroy()

    def test_encrypt(self):
        """Test text encryption."""
        self.app.is_encrypted = False
        self.app.text_var.set("Hello, World")

        self.app.toggle_cipher()

        self.assertEqual(self.app.entry_text.get(), "************")

    def test_decrypt(self):
        """Test text decryption."""
        self.app.is_encrypted = True
        self.app.saved_texts.append("Hello, World")
        self.app.text_var.set("************")

        self.app.toggle_cipher()

        self.assertEqual(self.app.entry_text.get(), "Hello, World")


if __name__ == "__main__":
    unittest.main()
