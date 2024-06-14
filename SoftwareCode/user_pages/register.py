from tkinter import *
import tkinter as tk
from tkinter import messagebox
from firebase_config import auth, database
from PIL import Image, ImageTk
import re

class RegisterPage:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root, bg='white')
        self.frame.pack(fill='both', expand=True)

        # Store references to PhotoImage objects
        self.images = {}
        # Dictionary to store input values
        self.input_values = {}

        # Load and resize the signup image
        self.images['signup_img'] = ImageTk.PhotoImage(Image.open('pictures/register picture.png').resize((598, 594), Image.Resampling.LANCZOS))
        signup_image_label = Label(self.frame, image=self.images['signup_img'], bg='white')
        signup_image_label.place(x=0, y=0)

        # Frame for Register Page
        register_frame = Frame(self.frame, width=450, height=550, bg='white')
        register_frame.place(x=600, y=30)

        # Load and resize the register title image
        self.images['register_title_img'] = ImageTk.PhotoImage(Image.open('pictures/Register An Account.png').resize((350, 40), Image.Resampling.LANCZOS))
        register_title_label = Label(register_frame, image=self.images['register_title_img'], bg='white')
        register_title_label.place(x=50, y=0)

        # Placeholder configuration
        placeholders_signup = [
            ("Name", 120),
            ("Email Address", 180),
            ("Phone Number", 240),
            ("Gender (Male/Female)", 300),
            ("Password", 360),
            ("Confirm Password", 420),
        ]

        # Function to clear placeholder text when clicked
        def clear_placeholder(event, entry, placeholder):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(foreground="black")

        # Function to restore placeholder text if entry is empty
        def restore_placeholder(event, entry, placeholder):
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(foreground="grey")

        self.images['entryfield_img'] = ImageTk.PhotoImage(Image.open('pictures/entryfield.png').resize((350, 50), Image.Resampling.LANCZOS))

        # Bind the functions to Entry widgets for signup fields
        for placeholder, y_coord in placeholders_signup:
            # Create a Canvas widget to place the image and entry field
            signup_canvas = Canvas(register_frame, width=350, height=50, bg='white', highlightthickness=0)
            signup_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
            signup_canvas.place(x=50, y=y_coord - 50)

            # Create the entry field and place it over the image on the canvas
            entry_placeholder = Entry(register_frame, width=28, fg='grey', border=0, bg='#ffffff', font=('Montserrat', 12, 'bold'))
            entry_placeholder.insert(0, placeholder)
            entry_placeholder.bind("<FocusIn>", lambda event, entry=entry_placeholder, placeholder=placeholder: clear_placeholder(event, entry, placeholder))
            entry_placeholder.bind("<FocusOut>", lambda event, entry=entry_placeholder, placeholder=placeholder: restore_placeholder(event, entry, placeholder))

            entry_placeholder.place(x=60, y=y_coord - 35)

            # Store the entry field in the input_values dictionary
            self.input_values[placeholder] = entry_placeholder

        # Load and resize the register button image
        self.images['register_button_img'] = ImageTk.PhotoImage(Image.open('pictures/register button.png').resize((250, 50), Image.Resampling.LANCZOS))

        # Function to validate email address
        def is_valid_email(email):
            return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

        # Function to handle register button click
        def handle_register():
            # Get input values from the dictionary
            c1 = self.input_values["Name"].get()
            c2 = self.input_values["Email Address"].get()
            c3 = self.input_values["Phone Number"].get()
            c4 = self.input_values["Gender (Male/Female)"].get()
            c5 = self.input_values["Password"].get()
            c6 = self.input_values["Confirm Password"].get()

            # validate for prompt input
            if any(value == "" for value in [c1, c2, c3, c4, c5, c6]):
                messagebox.showerror("Error", "All fields are required")
            elif not is_valid_email(c2):
                messagebox.showerror("Error", "Invalid email address format")
            elif not (c3.strip().isdigit() and 10 <= len(c3.strip()) <= 11):
                messagebox.showerror("Error", "Invalid contact number format")
            elif c4.upper() not in ['MALE', 'FEMALE']:
                messagebox.showerror("Error", "Invalid gender format")
            elif (c5 != "" and c6 != "") and (c5 != c6):
                messagebox.showerror("Error", "Both passwords must be the same")
            else:
                # Check if username or email already exists
                user_exists = True
                email_exists = True
                phone_exists = True
                for user in database.child("User").get().each():
                    if user.val()["username"] == c1:
                        user_exists = False
                    if user.val()["email"] == c2:
                        email_exists = False
                    if user.val()["phone"] == c2:
                        phone_exists = False

                if user_exists:
                    messagebox.showerror("Error", "Username already exists")
                elif email_exists:
                    messagebox.showerror("Error", "Email already exists")
                elif phone_exists:
                    messagebox.showerror("Error", "Phone number already exists")
                else:
                    # Save data to Firebase with a unique key
                    user_data = {
                        "username": c1,
                        "email": c2,
                        "phone": c3,
                        "gender": c4,
                        "password": c5
                    }
                    database.child("User").child(c1).set(user_data)
                    messagebox.showinfo("Success", "Registration successful!")
                    self.app.show_page("login")

        # Create the register button with the image and white background
        register_button = Button(register_frame, image=self.images['register_button_img'], command=handle_register, borderwidth=0, bg='white', activebackground='white')
        register_button.place(x=90, y=440)

        # Back to log in button on Signup Page
        back_to_login = Button(register_frame, text="Already have an account?", border=0, fg='black', bg='white', cursor='hand2', font=("Inter", 11, "bold"), command=lambda: self.app.show_page("login"))
        back_to_login.place(x=120, y=500)

