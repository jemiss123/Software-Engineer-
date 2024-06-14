import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *
from tkinter import ttk

# Initialize Firebase
cred = credentials.Certificate(r'C:\Users\User\PycharmProjects\DoctorPage\pythontkinter-91f78-firebase-adminsdk-okwv3-4f62f6cd21.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Tkinter
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
nav_homepage_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation homepage.png"
nav_homepage_img = PhotoImage(file=nav_homepage_image_path)
nav_homepage_label = Label(nav_frame, image=nav_homepage_img, bg='white')
nav_homepage_label.image = nav_homepage_img
nav_homepage_label.pack(pady=20)

# Load and display the navigation view patient records
nav_view_patient_records_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation viewpatientrecord.png"
nav_view_patient_records_img = PhotoImage(file=nav_view_patient_records_image_path)
nav_view_patient_records_label = Label(nav_frame, image=nav_view_patient_records_img, bg='white')
nav_view_patient_records_label.image = nav_view_patient_records_img
nav_view_patient_records_label.pack(pady=20)

# Load and display the navigation generate prescriptions
nav_generate_prescriptions_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation generateprescriptions.png"
nav_generate_prescriptions_img = PhotoImage(file=nav_generate_prescriptions_image_path)
nav_generate_prescriptions_label = Label(nav_frame, image=nav_generate_prescriptions_img, bg='white')
nav_generate_prescriptions_label.image = nav_generate_prescriptions_img
nav_generate_prescriptions_label.pack(pady=20)

# Load and display the logout image
nav_logout_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation logout.png"
nav_logout_img = PhotoImage(file=nav_logout_image_path)
nav_logout_label = Label(nav_frame, image=nav_logout_img, bg='white')
nav_logout_label.image = nav_logout_img
nav_logout_label.pack(side=BOTTOM, pady=(5, 20))  # Positioning at the bottom with padding

# Create frame for patient records section
record_frame = Frame(root, bg='white')
record_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Add heading
heading_label = Label(record_frame, text="Patient Records", font=("Arial", 18, "bold"), bg='white')
heading_label.pack(anchor='w', padx=50, pady=30)

# Load and display the header image
header_image_path = r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\patientrecords.png"
header_img = PhotoImage(file=header_image_path)
header_label = Label(record_frame, image=header_img, bg='white')
header_label.image = header_img
header_label.pack(fill='x')

# Run the application
root.mainloop()
