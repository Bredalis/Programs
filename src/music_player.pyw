
# Libraries
import pygame
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Playlist")
        self.window.geometry("210x100")
        self.window.resizable(0, 0)
        self.window.config(bg="#edd269")
        self.window.iconbitmap("../assets/images/song_logo.ico")
        self.playlist = []

        pygame.init()
        pygame.mixer.init()

        # Buttons
        tk.Button(
            self.window,
            text="Load",
            bg="#aee239",
            command=self.load_song
        ).pack()

        tk.Button(
            self.window,
            text="Play",
            bg="#aee239",
            command=self.play_song
        ).pack()

        tk.Button(
            self.window,
            text="Pause",
            bg="#aee239",
            command=self.pause_song
        ).pack()

        tk.Button(
            self.window,
            text="Resume",
            bg="#aee239",
            command=self.resume_song
        ).pack()

    def load_song(self):
        try:
            song = filedialog.askopenfilename(
                title="Music",
                initialdir="C:",
                filetypes=(
                    ("Audio files", "*.mp3"),
                    ("All files", "*.*")
                )
            )

            if song:
                self.playlist.append(song)

        except Exception as e:
            print(f"Unexpected error: {e}")

    def play_song(self):
        try:
            if not self.playlist:
                return

            pygame.mixer.music.load(self.playlist[0])
            pygame.mixer.music.play()

        except Exception as e:
            print(f"Unexpected error: {e}")

    def pause_song(self):
        pygame.mixer.music.pause()

    def resume_song(self):
        pygame.mixer.music.unpause()


if __name__ == "__main__":
    window = tk.Tk()
    app = MusicPlayer(window)
    window.mainloop()
