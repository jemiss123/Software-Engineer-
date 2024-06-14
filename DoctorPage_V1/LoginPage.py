import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase
cred = credentials.Certificate(r'C:\Users\User\PycharmProjects\DoctorPage\pythontkinter-91f78-firebase-adminsdk-okwv3-4f62f6cd21.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

from tkinter import *

root = Tk()
root.title('Homepage')
root.geometry('1331x594')  # Adjusted width to accommodate navigation section
root.configure(bg="#fff")
root.resizable(False, False)

# Create frame for navigation section
nav_frame = Frame(root, width=281, height=594, bg='white', highlightbackground="lightgrey", highlightthickness=1)
nav_frame.pack(side=LEFT, fill=Y)

# Load and display the navigation heading image
nav_heading_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation heading.png"
nav_heading_img = PhotoImage(file=nav_heading_image_path)
nav_heading_label = Label(nav_frame, image=nav_heading_img, bg='white')
nav_heading_label.image = nav_heading_img
nav_heading_label.pack(pady=20)

# Load and display the navigation home page
nav_heading_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation homepage.png"
nav_heading_img = PhotoImage(file=nav_heading_image_path)
nav_heading_label = Label(nav_frame, image=nav_heading_img, bg='white')
nav_heading_label.image = nav_heading_img
nav_heading_label.pack(pady=20)


# Load and display the navigation view patient records
nav_homepage_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation viewpatientrecord.png"
nav_homepage_img = PhotoImage(file=nav_homepage_image_path)
nav_homepage_label = Label(nav_frame, image=nav_homepage_img, bg='white')
nav_homepage_label.image = nav_homepage_img
nav_homepage_label.pack(pady=20)

# Load and display the navigation settings image
nav_settings_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation generateprescriptions.png"
nav_settings_img = PhotoImage(file=nav_settings_image_path)
nav_settings_label = Label(nav_frame, image=nav_settings_img, bg='white')
nav_settings_label.image = nav_settings_img
nav_settings_label.pack(pady=20)

# Load and display the logout image
nav_logout_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation logout.png"
nav_logout_img = PhotoImage(file=nav_logout_image_path)
nav_logout_label = Label(nav_frame, image=nav_logout_img, bg='white')
nav_logout_label.image = nav_logout_img
nav_logout_label.pack(side=BOTTOM, pady=(5, 20))  # Positioning at the bottom with padding

root.mainloop()
