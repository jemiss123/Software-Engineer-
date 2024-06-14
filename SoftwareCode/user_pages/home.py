import tkinter as tk
from tkinter import *


class HomePage:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root, bg='white')
        self.frame.pack(fill='both', expand=True)
        self.username = None

        # Add other widgets and setup here
        self.welcome_label = tk.Label(self.frame, text="", font=("Helvetica", 18))
        self.welcome_label.pack(pady=20)

    def set_username(self, username):
        self.username = username
        self.welcome_label.config(text=f"Welcome, {self.username}")

