from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from firebase_config import auth, database


class LoginPage:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root, bg='white')
        self.frame.pack(fill='both', expand=True)

        # Store references to PhotoImage objects
        self.images = {}

        # Load and resize the login image
        self.images['login_img'] = ImageTk.PhotoImage(Image.open('pictures/login.png').resize((598, 594), Image.Resampling.LANCZOS))
        login_image_label = Label(self.frame, image=self.images['login_img'], bg='white')
        login_image_label.place(x=0, y=0)

        # Frame for Login Page
        login_frame = Frame(self.frame, width=450, height=550, bg='white')
        login_frame.place(x=600, y=100)

        # Load and resize the login title image
        self.images['login_title_img'] = ImageTk.PhotoImage(Image.open('pictures/WELCOME to the best doctor provider system.png').resize((250, 50), Image.Resampling.LANCZOS))
        login_title_label = Label(self.frame, image=self.images['login_title_img'], bg='white')
        login_title_label.place(x=645, y=120)

        # Load and resize the email entry field box image
        self.images['entryfield_img'] = ImageTk.PhotoImage(Image.open('pictures/entryfield.png').resize((350, 50), Image.Resampling.LANCZOS))
        self.images['email_text_img'] = ImageTk.PhotoImage(Image.open('pictures/email text.png').resize((40, 15), Image.Resampling.LANCZOS))

        # Create a Canvas widget to place the image and entry field for email
        email_canvas = Canvas(self.frame, width=350, height=50, bg='black', highlightthickness=0)
        email_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
        email_canvas.place(x=650, y=220)

        # Create the email entry field and place it over the image on the canvas
        self.email_entry = Entry(self.frame, width=20, fg='black', border=0, bg='#ffffff', font=('Montserrat', 14))
        self.email_entry.place(x=670, y=230)  # Adjust the position to align with the image

        # Place the email text image on top of the entry field
        email_text_label = Label(self.frame, image=self.images['email_text_img'], bg='white')
        email_text_label.place(x=650, y=200)  # Adjust the position to align with the entry field

        # Load and resize the password text image
        self.images['password_text_img'] = ImageTk.PhotoImage(Image.open('pictures/password text.png').resize((70, 15), Image.Resampling.LANCZOS))

        # Create a Canvas widget to place the image and entry field for password
        password_canvas = Canvas(self.frame, width=350, height=50, bg='white', highlightthickness=0)
        password_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
        password_canvas.place(x=650, y=320)

        # Place the password text image on top of the password entry field
        password_text_label = Label(self.frame, image=self.images['password_text_img'], bg='white')
        password_text_label.place(x=650, y=300)  # Adjust the position to align with the entry field

        # Create the password entry field and place it over the image on the canvas
        self.password_entry = Entry(self.frame, width=20, fg='black', border=0, bg='#ffffff',
                                    font=('Montserrat', 14), show='*')
        self.password_entry.place(x=670, y=330)  # Adjust the position to align with the image

        # Function to toggle password visibility
        def toggle_password():
            if self.password_entry.cget('show') == '':
                self.password_entry.config(show='*')
                toggle_button.config(image=self.images['show_photo'])
            else:
                self.password_entry.config(show='')
                toggle_button.config(image=self.images['hide_photo'])

        self.images['show_photo'] = ImageTk.PhotoImage(Image.open('pictures/showpassword.png').resize((20, 20), Image.Resampling.LANCZOS))
        self.images['hide_photo'] = ImageTk.PhotoImage(Image.open('pictures/showpassword.png').resize((20, 20), Image.Resampling.LANCZOS))

        # Create the toggle button with the show image
        toggle_button = Button(self.frame, image=self.images['show_photo'], command=toggle_password,
                               borderwidth=0, bg='white', activebackground='white')
        toggle_button.place(x=970, y=335)  # Adjust position as needed

        # Load and resize the login button image
        self.images['button_photo'] = ImageTk.PhotoImage(Image.open('pictures/login button.png').resize((250, 50), Image.Resampling.LANCZOS))

        # Function to handle login button click
        def handle_login():
            c1 = self.email_entry.get()
            c2 = self.password_entry.get()

            if any(value == "" for value in [c1, c2]):
                messagebox.showerror("Error", "All fields are required")
            else:
                username_exists = True
                password_correct = True
                for user in database.child("User").get().each():
                    if user.val()["username"] == c1:
                        username_exists = False
                    if user.val()["password"] == c2:
                        password_correct = False

                if username_exists:
                    messagebox.showerror("Error", "Username not found")
                elif password_correct:
                    messagebox.showerror("Error", "Wrong password entered")
                else:
                    self.app.show_page("home", username=c1)

        # Create the login button with the image and white background
        login_button = Button(self.frame, image=self.images['button_photo'], command=handle_login,
                              borderwidth=0, bg='white', activebackground='white')
        login_button.place(x=700, y=430)  # Adjust x and y as needed

        # Forgot Password button
        forgot_password_button = Button(self.frame, text="Forgot Password?",
                                        command=lambda: self.app.show_page("forgotpassword"), bg='white', fg='black',
                                        font=('New Times Roman', 10, 'bold'), border=0)
        forgot_password_button.place(x=880, y=370)

        forgot_password_button = Button(self.frame, text="No account? Click here",
                                        command=lambda: self.app.show_page("register"), bg='white', fg='black',
                                        font=('New Times Roman', 12, 'bold'), border=0)
        forgot_password_button.place(x=730, y=520)


''' 
tk.Label(self.frame, text="Login Page", font=("Helvetica", 18)).pack(pady=20)
tk.Button(self.frame, text="Go to Home Page", command=lambda: self.app.show_page("home")).pack(pady=10)
tk.Button(self.frame, text="Go to Register Page", command=lambda: self.app.show_page("register")).pack(pady=10)
tk.Button(self.frame, text="Go to Forgot Password Page",
          command=lambda: self.app.show_page("forgotpassword")).pack(pady=10)
'''