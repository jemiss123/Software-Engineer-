# user homepage

import pyrebase
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk



class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Call Dr. Mini Program")
        self.root.geometry("1199x600")
        self.root.resizable(False, False)

        # BG Image
        self.bg = ImageTk.PhotoImage(file="images/welcomeImage.jpg")
        tk.Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # initialise the default page
        self.init_home_frame()
        self.show_home_frame()

    def init_home_frame(self):
        self.Frame_home = tk.Frame(self.root, bg="white")

        tk.Label(self.Frame_home, text="Call Dr. Home Page", font=("Impact", 15),
                 fg="black", bg="white").place(x=10, y=10)

        tk.Button(self.Frame_home, text="Home Page").place(x=10, y=50)
        tk.Button(self.Frame_home, text="Logout", command=self.logout_function).place(x=10, y=100)

    def show_home_frame(self):
        self.Frame_home.place(x=50, y=50, height=500, width=1100)

    def hide_home_frame(self):
        self.Frame_home.place_forget()

    def logout_function(self):
        self.hide_home_frame()
        app.show_login_frame()
