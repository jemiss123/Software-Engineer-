
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from firebase_config import auth, database

# concept: check with username and email address with database
# If successful, jump to reset password page, else showing error
# Jump to here ↓

class ResetPasswordPage:
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
        resetPassword_frame = Frame(self.frame, width=450, height=550, bg='white')
        resetPassword_frame.place(x=600, y=30)

        # Load and resize the forgot password title image
        self.images['forgotPassword_img'] = ImageTk.PhotoImage(Image.open('pictures/Reset Password.png').resize((300, 40), Image.Resampling.LANCZOS))
        self.images['entryfield_img'] = ImageTk.PhotoImage(Image.open('pictures/entryfield.png').resize((350, 50), Image.Resampling.LANCZOS))

        forgotPassword_title = Label(resetPassword_frame, image=self.images['forgotPassword_img'], bg='white')
        forgotPassword_title.place(x=70, y=20)


        self.images['password1_img'] = ImageTk.PhotoImage(
            Image.open('pictures/password text.png').resize((70, 15), Image.Resampling.LANCZOS))

        # Create a Canvas widget to place the image and entry field for username
        password1_canvas = Canvas(self.frame, width=350, height=50, bg='white', highlightthickness=0)
        password1_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
        password1_canvas.place(x=650, y=220)

        # Create the username entry field and place it over the image on the canvas
        self.password1_entry = Entry(self.frame, width=20, fg='black', border=0, bg='#ffffff',
                                    font=('New Times Roman', 14))
        self.password1_entry.place(x=670, y=230)  # Adjust the position to align with the image

        # Place the username text image on top of the entry field
        password1_text_label = Label(self.frame, image=self.images['password1_img'], bg='white')
        password1_text_label.place(x=650, y=200)  # Adjust the position to align with the entry field


        self.images['password2_img'] = ImageTk.PhotoImage(
            Image.open('pictures/ConfirmPassword.png').resize((100, 15), Image.Resampling.LANCZOS))

        # Create a Canvas widget to place the image and entry field for email or contact number
        password2_canvas = Canvas(self.frame, width=350, height=50, bg='white', highlightthickness=0)
        password2_canvas.create_image(0, 0, anchor=NW, image=self.images['entryfield_img'])
        password2_canvas.place(x=650, y=320)

        # Create the email entry field and place it over the image on the canvas
        self.password2_entry = Entry(self.frame, width=20, fg='black', border=0, bg='#ffffff', font=('New Times Roman', 14))
        self.password2_entry.place(x=670, y=330)  # Adjust the position to align with the image

        # Place the email text image on top of the entry field
        enter_password2_label = Label(self.frame, image=self.images['password2_img'], bg='white')
        enter_password2_label.place(x=650, y=300)  # Adjust the position to align with the entry field

        # Load and resize the register button image
        self.images['confirm_button_img'] = ImageTk.PhotoImage(
            Image.open('pictures/Confirm.png').resize((250, 50), Image.Resampling.LANCZOS))

        def get_username(self, username):
            self.username = username

        def handle_checking_data():
            username = self.app.get_shared_data("username")

            c1 = self.password1_entry.get()
            c2 = self.password2_entry.get()

            if any(value == "" for value in [c1, c2]):
                messagebox.showerror("Error", "All fields are required")
            elif c1 != c2:
                messagebox.showerror("Error", "Both must be same")
            else:
                database.child("User").child(username).child("password").set(c1)
                messagebox.showinfo("Success", "Password updated successfully")
                self.app.show_page("login")

        # Create the register button with the image and white background
        reset_button = Button(resetPassword_frame, image=self.images['confirm_button_img'], command=handle_checking_data,
                                 borderwidth=0, bg='white', activebackground='white')
        reset_button.place(x=90, y=440)

        # Back to log in button on Signup Page
        back_to_login = Button(resetPassword_frame, text="Already have an account?", border=0, fg='black', bg='white',
                               cursor='hand2', font=("New Times Roman", 11, "bold"), command=lambda: self.app.show_page("login"))
        back_to_login.place(x=120, y=500)



