import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import *
from tkinter import messagebox

# Initialize Firebase
cred = credentials.Certificate(r'C:\Users\User\PycharmProjects\DoctorPage_V1\pythontkinter-91f78-firebase-adminsdk-okwv3-4f62f6cd21.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythontkinter-91f78-default-rtdb.firebaseio.com/'
})

current_doctor_id = None

# Function to verify login credentials
def attempt_login(email, password):
    global current_doctor_id
    ref = db.reference('Doctor')
    doctors = ref.get()

    for doctor_id, doctor_info in doctors.items():
        if doctor_info['dc_email'] == email and doctor_info['dc_password'] == password:
            current_doctor_id = doctor_id
            load_main_application()
            return
    messagebox.showerror("Login Failed", "Invalid credentials")

# Function to load the main application after successful login
def load_main_application():
    login_frame.pack_forget()  # Remove the login frame
    register_frame.pack_forget()  # Remove the register frame if visible
    main_application()  # Load the main application

# Function to show the registration form
def show_register_form():
    login_frame.pack_forget()  # Hide login frame
    register_frame.pack(expand=True)  # Show register frame

# Function to register a new doctor
def register_doctor(email, password, name, phone):
    ref = db.reference('Doctor')
    new_doctor_id = ref.push().key  # Generate a new unique ID
    ref.child(new_doctor_id).set({
        'dc_email': email,
        'dc_password': password,
        'dc_name': name,
        'dc_phone': phone,
        'dc_id': new_doctor_id
    })
    messagebox.showinfo("Success", "Doctor registered successfully")
    register_frame.pack_forget()  # Hide register frame
    login_frame.pack(expand=True)  # Show login frame

# Initialize Tkinter
root = Tk()
root.title('Doctor Login')
root.geometry('400x400')
root.configure(bg="#fff")
root.resizable(False, False)

# Create login frame
login_frame = Frame(root, bg='white')
login_frame.pack(expand=True)

# Login form widgets
Label(login_frame, text="Doctor Login", font=("Arial", 18, "bold"), bg='white').pack(pady=20)

Label(login_frame, text="Email:", font=("Arial", 12), bg='white').pack(pady=5)
email_entry = Entry(login_frame, font=("Arial", 12), width=30)
email_entry.pack(pady=5)

Label(login_frame, text="Password:", font=("Arial", 12), bg='white').pack(pady=5)
password_entry = Entry(login_frame, font=("Arial", 12), show='*', width=30)
password_entry.pack(pady=5)

Button(login_frame, text="Login", font=("Arial", 12), command=lambda: attempt_login(email_entry.get(), password_entry.get())).pack(pady=10)
Button(login_frame, text="Register", font=("Arial", 12), command=show_register_form).pack(pady=10)

# Create register frame
register_frame = Frame(root, bg='white')

# Register form widgets
Label(register_frame, text="Doctor Registration", font=("Arial", 18, "bold"), bg='white').pack(pady=20)

Label(register_frame, text="Name:", font=("Arial", 12), bg='white').pack(pady=5)
name_entry = Entry(register_frame, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

Label(register_frame, text="Email:", font=("Arial", 12), bg='white').pack(pady=5)
reg_email_entry = Entry(register_frame, font=("Arial", 12), width=30)
reg_email_entry.pack(pady=5)

Label(register_frame, text="Password:", font=("Arial", 12), bg='white').pack(pady=5)
reg_password_entry = Entry(register_frame, font=("Arial", 12), show='*', width=30)
reg_password_entry.pack(pady=5)

Label(register_frame, text="Phone Number:", font=("Arial", 12), bg='white').pack(pady=5)
phone_entry = Entry(register_frame, font=("Arial", 12), width=30)
phone_entry.pack(pady=5)

Button(register_frame, text="Register", font=("Arial", 12), command=lambda: register_doctor(reg_email_entry.get(), reg_password_entry.get(), name_entry.get(), phone_entry.get())).pack(pady=20)
Button(register_frame, text="Back to Login", font=("Arial", 12), command=lambda: [register_frame.pack_forget(), login_frame.pack(expand=True)]).pack(pady=10)

def main_application():
    root.title('Homepage')
    root.geometry('1331x594')  # Adjusted width to accommodate navigation section

    # Create frame for navigation section
    nav_frame = Frame(root, width=281, height=594, bg='white', highlightbackground="lightgrey", highlightthickness=1)
    nav_frame.pack(side=LEFT, fill=Y)

    # Load images for navigation buttons
    nav_homepage_img = PhotoImage(file=r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation homepage.png")
    nav_view_patient_records_img = PhotoImage(file=r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation viewpatientrecord.png")
    nav_generate_prescriptions_img = PhotoImage(file=r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation generateprescriptions.png")
    nav_logout_img = PhotoImage(file=r"C:\Users\User\Desktop\Assignments\Degree Semester 2\Software Engineering\Software_Pictures\Pictures\HomePage\navigation logout.png")

    # Function to change button image on hover
    def on_enter(event):
        event.widget.config(image=event.widget.active_img)

    def on_leave(event):
        event.widget.config(image=event.widget.normal_img)

    # Navigation functions
    def show_homepage():
        for widget in record_frame.winfo_children():
            widget.destroy()
        heading_label = Label(record_frame, text="Upcoming Visit", font=("Arial", 18, "bold"), bg='white')
        heading_label.pack(anchor='w', padx=50, pady=30)
        fetch_appointment_data()

    def show_view_patient_records():
        for widget in record_frame.winfo_children():
            widget.destroy()
        heading_label = Label(record_frame, text="View Patient Records", font=("Arial", 18, "bold"), bg='white')
        heading_label.pack(anchor='w', padx=50, pady=30)
        fetch_patient_records()

    def show_generate_prescriptions():
        for widget in record_frame.winfo_children():
            widget.destroy()
        heading_label = Label(record_frame, text="Generate Prescriptions", font=("Arial", 18, "bold"), bg='white')
        heading_label.pack(anchor='w', padx=50, pady=30)

        # Create prescription form
        Label(record_frame, text="Patient Name:", font=("Arial", 12), bg='white').pack(pady=5)
        patient_name_entry = Entry(record_frame, font=("Arial", 12), width=30)
        patient_name_entry.pack(pady=5)

        Label(record_frame, text="User ID:", font=("Arial", 12), bg='white').pack(pady=5)
        user_id_entry = Entry(record_frame, font=("Arial", 12), width=30)
        user_id_entry.pack(pady=5)

        Button(record_frame, text="Fetch Details", font=("Arial", 12), command=lambda: fetch_patient_details(user_id_entry.get(), patient_name_entry.get(), patient_name_entry, appointment_date_entry)).pack(pady=10)

        Label(record_frame, text="Medications:", font=("Arial", 12), bg='white').pack(pady=5)
        medications_entry = Entry(record_frame, font=("Arial", 12), width=30)
        medications_entry.pack(pady=5)

        Label(record_frame, text="Instructions:", font=("Arial", 12), bg='white').pack(pady=5)
        instructions_entry = Entry(record_frame, font=("Arial", 12), width=30)
        instructions_entry.pack(pady=5)

        Label(record_frame, text="Appointment Date:", font=("Arial", 12), bg='white').pack(pady=5)
        appointment_date_entry = Entry(record_frame, font=("Arial", 12), width=30)
        appointment_date_entry.pack(pady=5)

        Button(record_frame, text="Submit", font=("Arial", 12), command=lambda: submit_prescription(
            patient_name_entry.get(),
            user_id_entry.get(),
            current_doctor_id,
            medications_entry.get(),
            instructions_entry.get(),
            appointment_date_entry.get()
        )).pack(pady=20)

    def logout():
        root.destroy()

    # Create navigation buttons
    nav_homepage_button = Button(nav_frame, image=nav_homepage_img, bg='white', borderwidth=0, command=show_homepage)
    nav_view_patient_records_button = Button(nav_frame, image=nav_view_patient_records_img, bg='white', borderwidth=0, command=show_view_patient_records)
    nav_generate_prescriptions_button = Button(nav_frame, image=nav_generate_prescriptions_img, bg='white', borderwidth=0, command=show_generate_prescriptions)
    nav_logout_button = Button(nav_frame, image=nav_logout_img, bg='white', borderwidth=0, command=logout)

    # Set active and normal images for buttons
    nav_homepage_button.normal_img = nav_homepage_img
    nav_homepage_button.active_img = nav_homepage_img  # Assuming same image for active state
    nav_view_patient_records_button.normal_img = nav_view_patient_records_img
    nav_view_patient_records_button.active_img = nav_view_patient_records_img  # Assuming same image for active state
    nav_generate_prescriptions_button.normal_img = nav_generate_prescriptions_img
    nav_generate_prescriptions_button.active_img = nav_generate_prescriptions_img  # Assuming same image for active state
    nav_logout_button.normal_img = nav_logout_img
    nav_logout_button.active_img = nav_logout_img  # Assuming same image for active state

    # Bind events for hover effect
    nav_homepage_button.bind("<Enter>", on_enter)
    nav_homepage_button.bind("<Leave>", on_leave)
    nav_view_patient_records_button.bind("<Enter>", on_enter)
    nav_view_patient_records_button.bind("<Leave>", on_leave)
    nav_generate_prescriptions_button.bind("<Enter>", on_enter)
    nav_generate_prescriptions_button.bind("<Leave>", on_leave)
    nav_logout_button.bind("<Enter>", on_enter)
    nav_logout_button.bind("<Leave>", on_leave)

    # Pack navigation buttons
    nav_homepage_button.pack(pady=20)
    nav_view_patient_records_button.pack(pady=20)
    nav_generate_prescriptions_button.pack(pady=20)
    nav_logout_button.pack(side=BOTTOM, pady=(5, 20))  # Positioning at the bottom with padding

    # Create frame for patient records section
    record_frame = Frame(root, bg='white')
    record_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # Function to fetch and display patient data
    def fetch_appointment_data():
        if not current_doctor_id:
            return

        ref = db.reference('Appointment')
        appointments = ref.get()

        for patient_id, appointment_data in appointments.items():
            if appointment_data.get('doctor_id') == current_doctor_id:
                display_appointment_record(patient_id, appointment_data)

    # Display at Upcoming Visits
    def display_appointment_record(patient_id, appointment_data):
        frame = Frame(record_frame, bg='white')
        frame.pack(fill=X, padx=50, pady=10)

        # Create and pack the label for "Patient ID"
        patient_id_label = Label(frame, text="Patient Name:", font=("Arial", 14), bg='white')
        patient_id_label.pack(side=LEFT)
        # Create and pack the actual patient ID
        id_label = Label(frame, text=patient_id, font=("Arial", 14), bg='white')
        id_label.pack(side=LEFT, padx=(0, 20))

        # Create and pack the label for "User ID" (assuming it's an email here)
        user_id_label = Label(frame, text="User ID:", font=("Arial", 14), bg='white')
        user_id_label.pack(side=LEFT)
        # Create and pack the actual user ID/email
        email_label = Label(frame, text=appointment_data.get('user_id', 'N/A'), font=("Arial", 14), bg='white')
        email_label.pack(side=LEFT, padx=(0, 20))

        # Create and pack the view detail button
        view_detail_button = Button(frame, text="View Detail",
                                    command=lambda: view_detail(patient_id, appointment_data))
        view_detail_button.pack(side=LEFT, padx=(20, 0))

    # Function to handle "View Detail" button click
    def view_detail(patient_id, appointment_data):
        # Handle view detail action (e.g., open new window with detailed info)
        detail_window = Toplevel(root)
        detail_window.title("Appointment Detail")
        detail_window.geometry("400x400")

        name_label = Label(detail_window, text=f"Patient ID: {patient_id}", font=("Arial", 14))
        name_label.pack(pady=10)

        user_id_label = Label(detail_window, text=f"User ID: {appointment_data.get('user_id', 'N/A')}", font=("Arial", 14))
        user_id_label.pack(pady=10)

        address_label = Label(detail_window, text=f"Address: {appointment_data.get('appointment_address', 'N/A')}", font=("Arial", 14))
        address_label.pack(pady=10)

        appointment_date_label = Label(detail_window, text=f"Appointment Date: {appointment_data.get('appointment_date', 'N/A')}", font=("Arial", 14))
        appointment_date_label.pack(pady=10)

        appointment_time_label = Label(detail_window, text=f"Appointment Time: {appointment_data.get('appointment_time', 'N/A')}", font=("Arial", 14))
        appointment_time_label.pack(pady=10)

        clinic_name_label = Label(detail_window, text=f"Clinic Name: {appointment_data.get('clinic_Name', 'N/A')}", font=("Arial", 14))
        clinic_name_label.pack(pady=10)

        status_label = Label(detail_window, text=f"Status: {'Confirmed' if appointment_data.get('status') else 'Pending'}", font=("Arial", 14))
        status_label.pack(pady=10)

    # Function to fetch patient details by user ID or patient name
    def fetch_patient_details(user_id, patient_name, patient_name_entry, appointment_date_entry):
        ref = db.reference('Appointment')
        appointments = ref.get()

        for patient_id, appointment_data in appointments.items():
            if appointment_data.get('user_id') == user_id or appointment_data.get('patient_name') == patient_name:
                patient_name_entry.delete(0, END)
                patient_name_entry.insert(0, appointment_data.get('patient_name', ''))
                appointment_date_entry.delete(0, END)
                appointment_date_entry.insert(0, appointment_data.get('appointment_date', ''))
                return
        messagebox.showerror("Error", "User ID or Patient Name not found")

    # Function to submit prescription data
    def submit_prescription(patient_name, user_id, doctor_id, medications, instructions, appointment_date):
        ref = db.reference('Prescriptions')
        new_prescription_id = ref.push().key  # Generate a new unique ID
        ref.child(new_prescription_id).set({
            'patient_name': patient_name,
            'user_id': user_id,
            'doctor_id': doctor_id,
            'medications': medications,
            'instructions': instructions,
            'appointment_date': appointment_date,
            'prescription_id': new_prescription_id
        })
        messagebox.showinfo("Success", "Prescription generated successfully")

    # Function to fetch and display patient records
    def fetch_patient_records():
        if not current_doctor_id:
            print("No doctor ID provided.")
            return

        try:
            ref = db.reference('Prescriptions')
            patient_records = ref.order_by_child('doctor_id').equal_to(current_doctor_id).get()
            print(f"Fetched patient records: {patient_records}")

            # Clear any existing records in the UI
            for widget in record_frame.winfo_children():
                widget.destroy()

            if not patient_records:
                no_records_label = Label(record_frame, text="No patient records found.", font=("Arial", 14), bg='white')
                no_records_label.pack(pady=20)
                return

            for patient_id, patient_data in patient_records.items():
                display_patient_record(patient_id, patient_data)

        except firebase_admin.exceptions.FirebaseError as e:
            print(f"Error fetching patient records: {e}")
            messagebox.showerror("Error", "Failed to fetch patient records. Please try again later.")

    def display_patient_record(patient_id, patient_data):
        frame = Frame(record_frame, bg='white')
        frame.pack(fill=X, padx=50, pady=10)

        name_label = Label(frame, text=f"Patient Name: {patient_data.get('patient_name', 'N/A')}", font=("Arial", 14),
                           bg='white')
        name_label.pack(side=LEFT, padx=(0, 20))

        user_id_label = Label(frame, text=f"User ID: {patient_data.get('user_id', 'N/A')}", font=("Arial", 14),
                              bg='white')
        user_id_label.pack(side=LEFT, padx=(0, 20))

        view_detail_button = Button(frame, text="View Detail", command=lambda: view_detail(patient_id, patient_data))
        view_detail_button.pack(side=LEFT, padx=(20, 0))

    #View detail for UPCOMING VISIT
    def view_detail(patient_id, patient_data):
        detail_window = Toplevel(root)
        detail_window.title("Patient Detail")
        detail_window.geometry("400x400")

        name_label = Label(detail_window, text=f"Patient Name: {patient_data.get('patient_name', 'N/A')}",
                           font=("Arial", 14))
        name_label.pack(pady=10)

        user_id_label = Label(detail_window, text=f"User ID: {patient_data.get('user_id', 'N/A')}", font=("Arial", 14))
        user_id_label.pack(pady=10)

        gender_label = Label(detail_window, text=f"Gender: {patient_data.get('gender', 'N/A')}", font=("Arial", 14))
        gender_label.pack(pady=10)

        appointment_date_label = Label(detail_window, text=f"Appointment Date: {patient_data.get('appointment_date', 'N/A')}",
                                font=("Arial", 14))
        appointment_date_label.pack(pady=10)

        appointment_address_label = Label(detail_window, text=f"Appointment Date: {patient_data.get('appointment_date', 'N/A')}",
                                font=("Arial", 14))
        appointment_address_label.pack(pady=10)

        desc_problems_label = Label(detail_window, text=f"Problem Described: {patient_data.get('desc_problems', 'N/A')}",
                                font=("Arial", 14))
        desc_problems_label.pack(pady=10)

        status_label = Label(detail_window, text=f"Status: {patient_data.get('status', 'N/A')}", font=("Arial", 14))
        status_label.pack(pady=10)

    # Function to show the generate prescriptions form
    def show_generate_prescriptions():
        for widget in record_frame.winfo_children():
            widget.destroy()
        heading_label = Label(record_frame, text="Generate Prescriptions", font=("Arial", 18, "bold"), bg='white')
        heading_label.pack(anchor='w', padx=50, pady=30)

        Label(record_frame, text="Patient Name:", font=("Arial", 12), bg='white').pack(pady=5)
        patient_name_entry = Entry(record_frame, font=("Arial", 12), width=30)
        patient_name_entry.pack(pady=5)

        Label(record_frame, text="User ID:", font=("Arial", 12), bg='white').pack(pady=5)
        user_id_entry = Entry(record_frame, font=("Arial", 12), width=30)
        user_id_entry.pack(pady=5)

        Button(record_frame, text="Fetch Details", font=("Arial", 12),
               command=lambda: fetch_patient_details(user_id_entry.get(), patient_name_entry.get(),
                                                     patient_name_entry)).pack(pady=10)

        Label(record_frame, text="Medications:", font=("Arial", 12), bg='white').pack(pady=5)
        medications_entry = Entry(record_frame, font=("Arial", 12), width=30)
        medications_entry.pack(pady=5)

        Label(record_frame, text="Instructions:", font=("Arial", 12), bg='white').pack(pady=5)
        instructions_entry = Entry(record_frame, font=("Arial", 12), width=30)
        instructions_entry.pack(pady=5)

        Label(record_frame, text="Appointment Date:", font=("Arial", 12), bg='white').pack(pady=5)
        appointment_date_entry = Entry(record_frame, font=("Arial", 12), width=30)
        appointment_date_entry.pack(pady=5)

        Button(record_frame, text="Submit", font=("Arial", 12), command=lambda: submit_prescription(
            patient_name_entry.get(),
            user_id_entry.get(),
            current_doctor_id,
            medications_entry.get(),
            instructions_entry.get(),
            appointment_date_entry.get()
        )).pack(pady=20)

    # Function to submit the prescription to the database
    def submit_prescription(user_name, user_id, doctor_id, medications, instructions, appointment_date):
        ref = db.reference('PatientRecords').child(user_id).child('Prescriptions')
        new_prescription_id = ref.push().key  # Generate a new unique ID
        ref.child(new_prescription_id).set({
            'patient_name': user_name,
            'user_id': user_id,
            'doctor_id': doctor_id,
            'medications': medications,
            'instructions': instructions,
            'appointment_date': appointment_date,
            'prescription_id': new_prescription_id
        })
        messagebox.showinfo("Success", "Prescription generated successfully")

    def display_patient_record(patient_id, patient_data):
        frame = Frame(record_frame, bg='white')
        frame.pack(fill=X, padx=50, pady=10)

        # Create and pack the label for "Patient Name"
        patient_name_label = Label(frame, text="Patient Name:", font=("Arial", 14), bg='white')
        patient_name_label.pack(side=LEFT)
        # Create and pack the actual patient name
        name_label = Label(frame, text=patient_data.get('patient_name', 'N/A'), font=("Arial", 14), bg='white')
        name_label.pack(side=LEFT, padx=(0, 20))

        # Create and pack the label for "User ID" (assuming it's an email here)
        user_id_label = Label(frame, text="User ID:", font=("Arial", 14), bg='white')
        user_id_label.pack(side=LEFT)
        # Create and pack the actual user ID/email
        email_label = Label(frame, text=patient_data.get('user_id', 'N/A'), font=("Arial", 14), bg='white')
        email_label.pack(side=LEFT, padx=(0, 20))

        # Create and pack the view detail button
        view_detail_button = Button(frame, text="View Detail",
                                    command=lambda: view_patient_detail(patient_id, patient_data))
        view_detail_button.pack(side=LEFT, padx=(20, 0))

    # Function to handle "View Detail" button click for patient records
    def view_patient_detail(patient_id, patient_data):
        # Handle view detail action (e.g., open new window with detailed info)
        detail_window = Toplevel(root)
        detail_window.title("Patient Detail")
        detail_window.geometry("400x400")

        name_label = Label(detail_window, text=f"Patient Name: {patient_data.get('patient_name', 'N/A')}", font=("Arial", 14))
        name_label.pack(pady=10)

        user_id_label = Label(detail_window, text=f"User ID: {patient_data.get('user_id', 'N/A')}", font=("Arial", 14))
        user_id_label.pack(pady=10)

        gender_label = Label(detail_window, text=f"Gender: {patient_data.get('gender', 'N/A')}", font=("Arial", 14))
        gender_label.pack(pady=10)

        doctor_label = Label(detail_window, text=f"Doctor ID: {patient_data.get('doctor_id', 'N/A')}", font=("Arial", 14))
        doctor_label.pack(pady=10)

        instructions_label = Label(detail_window, text=f"Instructions: {patient_data.get('Instructions', 'N/A')}", font=("Arial", 14))
        instructions_label.pack(pady=10)

        medications_label = Label(detail_window, text=f"Medications: {patient_data.get('Medications', 'N/A')}", font=("Arial", 14))
        medications_label.pack(pady=10)

        status_label = Label(detail_window, text=f"Status: {patient_data.get('status', 'N/A')}", font=("Arial", 14))
        status_label.pack(pady=10)

    # Show the homepage initially
    show_homepage()

# Run the application
root.mainloop()
