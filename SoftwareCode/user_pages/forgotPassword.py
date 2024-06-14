
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from firebase_config import auth, database

# concept: check with username and email address with database
# If successful, jump to reset password page, else showing error

class ForgotPasswordPage:
    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(self.app.root, bg='white')
        self.frame.pack(fill='both', expand=True)

        # Store references to PhotoImage objects
        self.images = {}

        # Load and resize the register title image
        self.images['signup_img'] = ImageTk.PhotoImage(
            Image.open('pictures/register picture.png').resize((598, 594), Image.Resampling.LANCZOS))
        signup_image_label = Label(self.frame, image=self.images['signup_img'], bg='white')
        signup_image_label.place(x=0, y=0)

        # Frame for ForgotPassword Page
        forgotPassword_frame = Frame(self.frame, width=450, height=550, bg='white')
        forgotPassword_frame.place(x=600, y=30)

        # Load and resize the forgot password title image
        self.images['forgotPassword_img'] = ImageTk.PhotoImage(Image.open('pictures/Forgot Password.png').resize((300, 40), Image.Resampling.LANCZOS))
        self.images['entryfield_img'] = ImageTk.PhotoImage(Image.open('pictures/entryfield.png').resize((350, 50), Image.Resampling.LANCZOS))

        forgotPassword_title = Label(forgotPassword_frame, image=self.images['forgotPassword_img'], bg='white')
        forgotPassword_title.place(x=70, y=20)


        self.images['username_img'] = ImageTk.PhotoImage(
            Image.open('pictures/username.png').resize((70, 15), Image.Resampling.LANCZOS))

        # Create a Canvas widget to place the image and entry field for username
        username_canvas = Canvas(self.frame, width=350, height=50, bg='white', highlightthickness=0)
        username_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
        username_canvas.place(x=650, y=220)

        # Create the username entry field and place it over the image on the canvas
        self.username_entry = Entry(self.frame, width=20, fg='black', border=0, bg='#ffffff',
                                    font=('New Times Roman', 14))
        self.username_entry.place(x=670, y=230)  # Adjust the position to align with the image

        # Place the username text image on top of the entry field
        username_text_label = Label(self.frame, image=self.images['username_img'], bg='white')
        username_text_label.place(x=650, y=200)  # Adjust the position to align with the entry field

        self.images['email_img'] = ImageTk.PhotoImage(
            Image.open('pictures/email.png').resize((100, 15), Image.Resampling.LANCZOS))

        # Create a Canvas widget to place the image and entry field for email or contact number
        email_canvas = Canvas(self.frame, width=350, height=50, bg='white', highlightthickness=0)
        email_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
        email_canvas.place(x=650, y=320)

        # Create the email entry field and place it over the image on the canvas
        self.email_entry = Entry(self.frame, width=20, fg='black', border=0, bg='#ffffff', font=('New Times Roman', 14))
        self.email_entry.place(x=670, y=330)  # Adjust the position to align with the image

        # Place the email text image on top of the entry field
        enter_email_label = Label(self.frame, image=self.images['email_img'], bg='white')
        enter_email_label.place(x=650, y=300)  # Adjust the position to align with the entry field

        # Load and resize the register button image
        self.images['confirm_button_img'] = ImageTk.PhotoImage(
            Image.open('pictures/Confirm.png').resize((250, 50), Image.Resampling.LANCZOS))

        def handle_checking_data():
            c1 = self.username_entry.get()
            c2 = self.email_entry.get()

            if any(value == "" for value in [c1, c2]):
                messagebox.showerror("Error", "All fields are required")
            else:
                username_exists = True
                email_correct = True
                for user in database.child("User").get().each():
                    if user.val()["username"] == c1:
                        username_exists = False
                    if user.val()["email"] == c2:
                        email_correct = False

                if username_exists:
                    messagebox.showerror("Error", "Username not found")
                elif email_correct:
                    messagebox.showerror("Error", "Email not found")
                else:
                    self.app.show_page("resetpassword", username=c1)

        # Create the register button with the image and white background
        reset_button = Button(forgotPassword_frame, image=self.images['confirm_button_img'], command=handle_checking_data,
                                 borderwidth=0, bg='white', activebackground='white')
        reset_button.place(x=90, y=440)

        # Back to log in button on Signup Page
        back_to_login = Button(forgotPassword_frame, text="Already have an account?", border=0, fg='black', bg='white',
                               cursor='hand2', font=("New Times Roman", 11, "bold"), command=lambda: self.app.show_page("login"))
        back_to_login.place(x=120, y=500)



