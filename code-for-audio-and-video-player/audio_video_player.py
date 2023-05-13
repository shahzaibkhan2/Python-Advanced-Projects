# Importing necessary modules
import tkinter as tk
from tkinter import filedialog
import pygame

# player class
class Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Shahzaib Audio and Video Player")
        self.root.geometry("500x300")

        self.filename = ""

        # Create buttons
        self.open_button = tk.Button(self.root, text="Open", command=self.open_file)
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)

        # Create video canvas
        self.canvas = tk.Canvas(self.root, width=400, height=225)

        # Place buttons and canvas
        self.open_button.pack(pady=10)
        self.play_button.pack(side=tk.LEFT, padx=10)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        self.canvas.pack(pady=10)

    # A function to open files
    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("Audio files", "*.mp3;*.wav"),
                                                              ("Video files", "*.mp4;*.avi")))

    # A function to play file
    def play(self):
        if self.filename:
            pygame.mixer.init()
            pygame.mixer.music.load(self.filename)
            pygame.mixer.music.play()

    # A function to pause the file
    def pause(self):
        if self.filename:
            pygame.mixer.music.pause()

    # A function to stop the file
    def stop(self):
        if self.filename:
            pygame.mixer.music.stop()

# main root area to run tkinter mainloop
root = tk.Tk()
player = Player(root)
root.mainloop()
