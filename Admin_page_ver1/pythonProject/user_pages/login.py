from pythonProject.pythonProject.main import firebaseConfig
import random
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import random
# using 'pip install twilio' to install package for receive OTP
from twilio.rest import Client
# using 'pip install python-dotenv' to install


import pyrebase


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

class Login:
    def __init__(self, root, home_instance):
        self.root = root
        # link to home page
        self.home_instance = home_instance
        self.root.title("Call Dr. Mini Program")
        self.root.geometry("1199x600")
        self.root.resizable(False, False)

        # BG Image
        self.bg = ImageTk.PhotoImage(file="images/welcomeImage.jpg")
        tk.Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Initialize frames
        self.init_login_frame()
        self.init_register_frame()
        self.init_resetPassword_frame()
        self.init_getOtp_frame()

        # default the first page is login_frame
        self.show_login_frame()

    # variable = txt_user, txt_pass, login_btn
    # functional button = login_btn
    def init_login_frame(self):
        self.Frame_login = tk.Frame(self.root, bg="white")

        # page title with describe
        tk.Label(self.Frame_login, text="WELCOME", font=("Impact", 25, "bold"), fg="#d77337", bg="white").place(x=130,
                                                                                                                y=30)
        tk.Label(self.Frame_login, text="TO CALL DR. MINI PROGRAM", font=("Goudy old style", 15),
                 fg="#d25d17", bg="white").place(x=130, y=80)

        # username enter
        tk.Label(self.Frame_login, text="Username", font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(
            x=130, y=140)
        self.txt_user = tk.Entry(self.Frame_login, font=("times new roman", 15), bg="#D8D8D8")
        self.txt_user.place(x=130, y=170, width=300, height=35)

        # password enter
        tk.Label(self.Frame_login, text="Password", font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(
            x=130, y=210)
        self.txt_pass = tk.Entry(self.Frame_login, font=("times new roman", 15), bg="#D8D8D8", show="*")
        self.txt_pass.place(x=130, y=240, width=300, height=35)

        # button for reset password
        tk.Button(self.Frame_login, text="Forget Password", bg="white", fg="#d77337", bd=0,
                  font=("times new roman", 12), command=self.show_resetPassword_frame).place(x=310, y=280)

        # button for register
        tk.Button(self.Frame_login, text="Register an account for free!", bg="white", fg="#d77337",
                  bd=0, font=("times new roman", 12), command=self.show_register_frame).place(x=160, y=330)

        # button with login, this button difference because of the design
        self.login_btn = tk.Button(self.Frame_login, text="Login", cursor="hand2", fg="white", bg="#d77337",
                                   font=("times new roman", 20), command=self.login_function)
        self.login_btn.place(x=160, y=370, width=180, height=40)

    # variable = lbl_reg_user, lbl_reg_email, lbl_reg_phone, gender_val, lbl_reg_password, lbl_reg_password2
    # functional button = register_btn
    def init_register_frame(self):
        self.Frame_register = tk.Frame(self.root, bg="white")

        # title
        tk.Label(self.Frame_register, text="Register An Account", font=("Impact", 25, "bold"), fg="#d77337",
                 bg="white").place(x=90, y=30)

        # enter username
        tk.Label(self.Frame_register, text="Username", font=("Goudy old style", 10, "bold"), fg="gray",
                 bg="white").place(x=90, y=100)
        self.lbl_reg_user = tk.Entry(self.Frame_register, font=("times new roman", 15), bg="#D8D8D8")
        self.lbl_reg_user.place(x=220, y=100, width=300, height=30)

        # enter email address
        tk.Label(self.Frame_register, text="Email Address", font=("Goudy old style", 10, "bold"), fg="gray",
                 bg="white").place(x=90, y=140)
        self.lbl_reg_email = tk.Entry(self.Frame_register, font=("times new roman", 15), bg="#D8D8D8")
        self.lbl_reg_email.place(x=220, y=140, width=300, height=30)

        # enter phone number
        tk.Label(self.Frame_register, text="Phone Number", font=("Goudy old style", 10, "bold"), fg="gray",
                 bg="white").place(x=90, y=180)
        self.lbl_reg_phone = tk.Entry(self.Frame_register, font=("times new roman", 15), bg="#D8D8D8")
        self.lbl_reg_phone.place(x=220, y=180, width=300, height=30)

        # choose gender
        tk.Label(self.Frame_register, text="Gender", font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(
            x=90, y=220)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Choose your gender")
        tk.OptionMenu(self.Frame_register, self.gender_var, "Male", "Female", "Not rather to say").place(x=220, y=220, width=300, height=30)

        # enter password
        tk.Label(self.Frame_register, text="Password", font=("Goudy old style", 10, "bold"), fg="gray",
                 bg="white").place(x=90, y=260)
        self.lbl_reg_password = tk.Entry(self.Frame_register, font=("times new roman", 15), bg="#D8D8D8", show="*")
        self.lbl_reg_password.place(x=220, y=260, width=300, height=30)

        # enter second-time password
        tk.Label(self.Frame_register, text="Confirm Password", font=("Goudy old style", 10, "bold"), fg="gray",
                 bg="white").place(x=90, y=300)
        self.lbl_reg_password2 = tk.Entry(self.Frame_register, font=("times new roman", 15), bg="#D8D8D8", show="*")
        self.lbl_reg_password2.place(x=220, y=300, width=300, height=30)

        # button for return back to login page
        tk.Button(self.Frame_register, text="Already have an account? Just SignIn", bg="white", fg="#d77337", bd=0,
                  font=("times new roman", 12), command=self.show_login_frame).place(x=130, y=335)

        # button with register, this button difference because of the design
        self.register_btn = tk.Button(self.Frame_register, text="Register", fg="white", bg="#d77337",
                                      font=("times new roman", 20), command=self.register_function)
        self.register_btn.place(x=160, y=370, width=180, height=40)

    # variable = txt_key, txt_otp
    # functional button = request_otp_btn, request_btn
    def init_resetPassword_frame(self):
        self.Frame_resetPassword = tk.Frame(self.root, bg="white")

        # title
        tk.Label(self.Frame_resetPassword, text="Reset Password", font=("Impact", 25, "bold"),
                 fg="#d77337", bg="white").place(x=130, y=30)

        # try to make it reset password using either email or password, both will sent OTP for verification
        tk.Label(self.Frame_resetPassword, text="Enter Email Address or Phone Number for request OTP",
                 font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(x=130, y=120)
        self.txt_key = tk.Entry(self.Frame_resetPassword, font=("times new roman", 15), bg="#D8D8D8")
        self.txt_key.place(x=130, y=150, width=350, height=35)

        # enter OTP
        tk.Label(self.Frame_resetPassword, text="Enter OTP",
                 font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(x=130, y=200)
        self.txt_otp = tk.Entry(self.Frame_resetPassword, font=("times new roman", 15), bg="#D8D8D8")
        self.txt_otp.place(x=130, y=230, width=250, height=35)

        # button for getting the auth of OTP from input, checking input auth with firebase
        self.request_otp_btn = tk.Button(self.Frame_resetPassword, text="Request OTP", bg="white", fg="#0D0C0C",
                  bd=0, font=("times new roman", 12), command=self.checking_otp_function)
        self.request_otp_btn.place(x=380, y=230)

        # button for return back login page from reset password page
        tk.Button(self.Frame_resetPassword, text="Back to login page", bg="white", fg="#d77337",
                  bd=0, font=("times new roman", 12), command=self.show_login_frame).place(x=220, y=300)

        # button for checking the auth of OTP and return to reset password page
        self.request_btn = tk.Button(self.Frame_resetPassword, text="Confirm", fg="white", bg="#d77337",
                                     font=("times new roman", 12), command=self.checking_new_password)
        self.request_btn.place(x=200, y=340, width=180, height=40)

    # variable = txt_reset_password, txt_reset_password2
    # functional button = confirm_btn
    def init_getOtp_frame(self):
        self.Frame_getOtp = tk.Frame(self.root, bg="white")

        # title
        # get the OTP after verification
        tk.Label(self.Frame_getOtp, text="Reset Password", font=("Impact", 25, "bold"),
                 fg="#d77337", bg="white").place(x=130, y=30)

        # enter a new password
        tk.Label(self.Frame_getOtp, text="Enter new password",
                 font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(x=130, y=130)
        self.txt_reset_password = tk.Entry(self.Frame_getOtp, font=("times new roman", 15), bg="#D8D8D8", show="*")
        self.txt_reset_password.place(x=130, y=160, width=350, height=35)

        # enter second-time password
        tk.Label(self.Frame_getOtp, text="Confirm new password",
                 font=("Goudy old style", 10, "bold"), fg="gray", bg="white").place(x=130, y=210)
        self.txt_reset_password2 = tk.Entry(self.Frame_getOtp, font=("times new roman", 15), bg="#D8D8D8", show="*")
        self.txt_reset_password2.place(x=130, y=240, width=350, height=35)

        # if the OTP is correct will messagebox.showInfo that password have successfully updated
        self.confirm_btn = tk.Button(self.Frame_getOtp, text="Confirm", fg="white", bg="#d77337",
                                     font=("times new roman", 12), command=self.show_login_frame)
        self.confirm_btn.place(x=200, y=330, width=180, height=40)

    def show_login_frame(self):
        # able to return back into those page
        self.Frame_register.place_forget()
        self.Frame_resetPassword.place_forget()
        self.Frame_getOtp.place_forget()
        self.Frame_login.place(x=150, y=110, height=420, width=600)

    def show_register_frame(self):
        # able to return back into those page
        self.Frame_login.place_forget()
        self.Frame_register.place(x=150, y=110, height=420, width=600)

    def show_resetPassword_frame(self):
        # able to return back into those page
        self.Frame_login.place_forget()
        self.Frame_resetPassword.place(x=150, y=110, height=420, width=600)

    def show_getOtp_frame(self):
        # able to return back into those page
        self.Frame_login.place_forget()
        self.Frame_getOtp.place(x=150, y=110, height=420, width=600)

    # done validate with firebase only the existed username and password will enter to home page
    # any left validation just inform me (-> wei ming)
    def login_function(self):
        # for avoid empty validation
        c1 = self.txt_user.get()
        c2 = self.txt_pass.get()

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

                self.Frame_login.place_forget()
                self.home_instance.show_home_frame()

    # done validate with firebase only accepted those haven't register data and insert new data into firebase
    # any left validation just inform me (-> wei ming)
    def register_function(self):
        c1 = self.lbl_reg_user.get()
        c2 = self.lbl_reg_email.get()
        c3 = self.lbl_reg_phone.get()
        c4 = self.gender_var.get()
        c5 = self.lbl_reg_password.get()
        c6 = self.lbl_reg_password2.get()
        c7 = random.randint(00000,99999)

        # validate for prompt input
        if any(value == "" for value in [c1, c2, c3, c4, c5, c6]):
            messagebox.showerror("Error", "All fields are required")
        elif c5 != c6:
            messagebox.showerror("Error", "Both passwords must be the same")

        else:
            # Check if username or email already exists
            user_exists = False
            email_exists = False
            phone_exists = False
            userId_exists =False
            for user in database.child("User").get().each():
                if user.val()["username"] == c1:
                    user_exists = True
                if user.val()["email"] == c2:
                    email_exists = True
                if user.val()["phone"] == c2:
                    phone_exists = True
                if userId_exists['user_id'] == c7:
                    userId_exists = True

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
                    "password": c5,
                    "user_id": c7
                }
                database.child("User").child(c7).set(user_data)
                messagebox.showinfo("Success", "Registration successful!")
                self.Frame_login.place_forget()
                self.show_login_frame()

    # function still empty for reset password page - request otp element
    def checking_otp_function(self):
        # Generate OTP (between 0000-9999)
        otp = str(random.randint(0000, 9999))
        c1 = self.txt_key.get()
        c2 = self.txt_otp.get()

        if any(value == "" for value in [c1, c2]):
            messagebox.showerror("Error", "All fields are required")
        '''else:
            email_exists = False
            phone_exists = False
            user_data = None

            # Check if username or email exists
            for user in database.child("User").get().each():
                if user.val()["email"] == c1:
                    email_exists = True
                    user_data = user.val()
                    break
                if user.val()["phone"] == c1:
                    phone_exists = True
                    user_data = user.val()
                    break

            # If user exists, send OTP
            if email_exists or phone_exists:
                # Assume OTP is sent via email
                # If the user has phone number, send OTP via SMS
                if "phone" in user_data:
                    # send_sms_otp(user_data["phone"], otp)
                else:
                    # send_email_otp(c1, otp)

                # Assuming OTP verification happens elsewhere,
                # you might want to open a new window to verify OTP
                # and update password or return to reset password page
                # based on the verification result
                # For simplicity, just showing a messagebox here
                messagebox.showinfo("OTP Sent", "OTP has been sent for verification.")
            else:
                messagebox.showerror("Error", "User or email not found")'''

    # function still empty for reset password page - after auth OTP and changing a new password
    def checking_new_password(self):
        pass


'''    def register_function(self):
        c1 = self.lbl_reg_user.get()
        c2 = self.lbl_reg_email.get()
        c3 = self.lbl_reg_phone.get()
        c4 = self.gender_var.get()
        c5 = self.lbl_reg_password.get()
        c6 = self.lbl_reg_password2.get()



        # validate for prompt input
        if any(value == "" for value in [c1, c2, c3, c4, c5, c6]):
            messagebox.showerror("Error", "All fields are required")

        elif c1 == database.child("User").child("username"):
            messagebox.showerror("Error", "Username has been already existed")

        elif c2 == database.child("User").child("email"):
            messagebox.showerror("Error", "Email has been already existed")

        elif c3 == database.child("User").child("phone"):
            messagebox.showerror("Error", "Phone has been already existed")

        elif c5 != c6:
            messagebox.showerror("Error", "Both password must be same")

        else:
            data = {"username": c1, "email": c2, "phone": c3, "gender": c4, "password": c5}
            database.child("User").push(data)
            self.Frame_login.place_forget()
            self.home_instance.show_home_frame()'''
