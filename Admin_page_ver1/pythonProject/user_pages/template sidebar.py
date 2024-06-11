'''from pathlib import Path
from tkinter import Tk, Frame, Button, BOTH, LEFT, TOP, NSEW, CENTER, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
# pythonProject.pythonProject.main import firebaseConfig
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyDH92FCT2_eZozopA67rE6giVtNtPJEzxw",
    "authDomain": "pythontkinter-91f78.firebaseapp.com",
    "databaseURL": "https://pythontkinter-91f78-default-rtdb.firebaseio.com/",
    "projectId": "pythontkinter-91f78",
    "storageBucket": "pythontkinter-91f78.appspot.com",
    "messagingSenderId": "483196256806",
    "appId": "1:483196256806:web:27ac629ed5050e6c759ce7",
    "measurementId": "G-VENQ3J95XH"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

PATH = Path(__file__).parent

class Cleaner(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=True)

        # Function to resize images
        def resize_image(image_path, size):
            img = Image.open(image_path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        # Application images
        self.images = {
            'Manage_request': resize_image("C:/Users/ACER/Documents/Sem 2 - Software-Engineer/Assignment/pythonProject/pythonProject/images/mng.reqst.png", (50, 50)),
            'Doctor': resize_image("C:/Users/ACER/Documents/Sem 2 - Software-Engineer/Assignment/pythonProject/pythonProject/images/doctor.png",(50, 50)),
            'setting': resize_image("C:/Users/ACER/Documents/Sem 2 - Software-Engineer/Assignment/pythonProject/pythonProject/images/setting.png", (50, 50)),
            'privacy': resize_image(PATH / 'home.png', (50, 50)),
            'junk': resize_image(PATH / 'home.png', (50, 50)),
            'protect': resize_image(PATH / 'home.png', (50, 50))
        }

        # Action buttons
        action_frame = Frame(self, padx=30, pady=30, bg='white')
        action_frame.grid(row=1, column=0, sticky=NSEW)

        home_btn = Button(
            master=action_frame,
            image=self.images['Manage_request'],
            text='Manage Request',
            compound=LEFT,
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#5D7285",
            activebackground="#0C7FDA",
            activeforeground="#5D7285",
            padx=30,
            pady=10,
            relief="flat",
            borderwidth=0
        )
        home_btn.pack(side=TOP, fill=BOTH, ipadx=30, ipady=10)

        doctor_btn = Button(
            master=action_frame,
            image=self.images['Doctor'],
            text='Manage Doctor',
            compound=LEFT,
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#5D7285",
            activebackground="#0C7FDA",
            activeforeground="#5D7285",
            padx=35,
            pady=10,
            relief="flat",
            borderwidth=0
        )
        doctor_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        setting_btn = Button(
            master=action_frame,
            image=self.images['setting'],
            text='System Setting',
            compound=LEFT,
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#5D7285",
            activebackground="#0C7FDA",
            activeforeground="#5D7285",
            padx=35,
            pady=10,
            relief="flat",
            borderwidth=0
        )
        setting_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        # Table frame
        table_frame = Frame(self, padx=30, pady=30)
        table_frame.grid(row=1, column=1, columnspan=2, sticky=NSEW)

        # Style the Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        background="#F5F5F5",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#F5F5F5",
                        font=('Arial', 12))
        style.configure("Treeview.Heading",
                        background="#0C7FDA",
                        font=('Arial', 12, 'bold'))
        style.map('Treeview',
                  background=[('selected', '#0C7FDA')])

        # Sample data
        data = [
            ("2024-06-04", "10:00", "John Doe", "Dr. Smith", "Clinic A"),
            ("2024-06-04", "11:00", "Jane Doe", "Dr. Brown", "Clinic B"),
            ("2024-06-04", "12:00", "Alice Smith", "Dr. White", "Clinic C"),
            ("2024-06-04", "13:00", "Bob Johnson", "Dr. Green", "Clinic D"),
            #(database.child('User').child('username').get(),database.child('User').child('gender'),database.child('User').child('email')),
            #(database.child('User').get(),"abc"),

        ]

        # Create table
        columns = ("Date", "Time", "Patient Name", "Doctor Name", "Clinic Name", "Status")
        tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        # Define headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor=CENTER)

        # Insert data into the table
        for row in data:
            tree.insert('', 'end', values=row + ("Pending",))

        # Function to show a dialog box for status change
        def change_status_dialog(item):
            result = messagebox.askquestion(
                "Change Status",
                "Do you want to accept or reject this request?",
                icon='question'
            )

            if result == 'yes':
                result = messagebox.askyesnocancel(
                    "Select Action",
                    "Do you want to Accept?",
                    icon='question'
                )
                if result is True:
                    tree.set(item, "Status", "Accepted")

                elif result is False:
                    tree.set(item, "Status", "Rejected")
                else:
                    pass  # User cancelled

        # Bind mouse click to handle status change
        def on_tree_select(event):
            selected_item = tree.selection()
            if selected_item:
                selected_index = tree.index(selected_item)
                if tree.identify_region(event.x, event.y) == "cell":
                    column = tree.identify_column(event.x)
                    if column == "#6":
                        change_status_dialog(selected_item)

        tree.bind("<Button-1>", on_tree_select)

        # Configure grid weights to make layout responsive
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)

if __name__ == '__main__':
    app = Tk()
    app.title("PC Cleaner")
    Cleaner(app)
    app.mainloop()
'''

from pathlib import Path
from tkinter import Tk, Frame, Button, BOTH, LEFT, TOP, NSEW, CENTER, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
# pythonProject.pythonProject.main import firebaseConfig

import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDH92FCT2_eZozopA67rE6giVtNtPJEzxw",
    "authDomain": "pythontkinter-91f78.firebaseapp.com",
    "databaseURL": "https://pythontkinter-91f78-default-rtdb.firebaseio.com/",
    "projectId": "pythontkinter-91f78",
    "storageBucket": "pythontkinter-91f78.appspot.com",
    "messagingSenderId": "483196256806",
    "appId": "1:483196256806:web:27ac629ed5050e6c759ce7",
    "measurementId": "G-VENQ3J95XH"
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

PATH = Path(__file__).parent

class Cleaner(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=True)

        # Function to resize images
        def resize_image(image_path, size):
            img = Image.open(image_path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        # Application images
        self.images = {
            'Manage_request': resize_image("C:/Users/ACER/Documents/Sem 2 - Software-Engineer/Assignment/pythonProject/pythonProject/images/mng.reqst.png", (50, 50)),
            'Doctor': resize_image("C:/Users/ACER/Documents/Sem 2 - Software-Engineer/Assignment/pythonProject/pythonProject/images/doctor.png", (50, 50)),
            'setting': resize_image("C:/Users/ACER/Documents/Sem 2 - Software-Engineer/Assignment/pythonProject/pythonProject/images/setting.png", (50, 50)),
            'privacy': resize_image(PATH / 'home.png', (50, 50)),
            'junk': resize_image(PATH / 'home.png', (50, 50)),
            'protect': resize_image(PATH / 'home.png', (50, 50))
        }

        # Action buttons
        action_frame = Frame(self, padx=30, pady=30, bg='white')
        action_frame.grid(row=1, column=0, sticky=NSEW)

        home_btn = Button(
            master=action_frame,
            image=self.images['Manage_request'],
            text='Manage Request',
            compound=LEFT,
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#5D7285",
            activebackground="#0C7FDA",
            activeforeground="#5D7285",
            padx=30,
            pady=10,
            relief="flat",
            borderwidth=0
        )
        home_btn.pack(side=TOP, fill=BOTH, ipadx=30, ipady=10)

        doctor_btn = Button(
            master=action_frame,
            image=self.images['Doctor'],
            text='Manage Doctor',
            compound=LEFT,
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#5D7285",
            activebackground="#0C7FDA",
            activeforeground="#5D7285",
            padx=35,
            pady=10,
            relief="flat",
            borderwidth=0
        )
        doctor_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        setting_btn = Button(
            master=action_frame,
            image=self.images['setting'],
            text='System Setting',
            compound=LEFT,
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#5D7285",
            activebackground="#0C7FDA",
            activeforeground="#5D7285",
            padx=35,
            pady=10,
            relief="flat",
            borderwidth=0
        )
        setting_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        # Table frame
        table_frame = Frame(self, padx=30, pady=30)
        table_frame.grid(row=1, column=1, columnspan=2, sticky=NSEW)

        # Style the Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        background="#F5F5F5",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#F5F5F5",
                        font=('Arial', 12))
        style.configure("Treeview.Heading",
                        background="#0C7FDA",
                        font=('Arial', 12, 'bold'))
        style.map('Treeview',
                  background=[('selected', '#0C7FDA')])

        # Create table
        columns = ("Date", "Time", "Patient Name", "Doctor Name", "Clinic Name", "Status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor=CENTER)

        # Insert data into the table
        self.fetch_and_insert_data()

        # Function to show a dialog box for status change
        def change_status_dialog(item):
            result = messagebox.askquestion(
                "Change Status",
                "Do you want to accept or reject this request?",
                icon='question'
            )

            if result == 'yes':
                result = messagebox.askyesnocancel(
                    "Select Action",
                    "Do you want to Accept?",
                    icon='question'
                )
                if result is True:
                    self.tree.set(item, "Status", "Accepted")
                elif result is False:
                    self.tree.set(item, "Status", "Rejected")
                else:
                    pass  # User cancelled

        # Bind mouse click to handle status change
        def on_tree_select(event):
            selected_item = self.tree.selection()
            if selected_item:
                if self.tree.identify_region(event.x, event.y) == "cell":
                    column = self.tree.identify_column(event.x)
                    if column == "#6":
                        change_status_dialog(selected_item[0])

        self.tree.bind("<Button-1>", on_tree_select)

        # Configure grid weights to make layout responsive
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)

    def fetch_and_insert_data(self):
        try:
            users = database.child('User').get()

            if users.each():
                for user in users.each():
                    user_data = user.val()
                    row = (
                        "2024-06-04",  # Date (example static value, replace as needed)
                        "10:00",       # Time (example static value, replace as needed)
                        user_data.get('gender', 'N/A'),
                        "Dr. Smith",   # Doctor Name (example static value, replace as needed)
                        "Clinic A",    # Clinic Name (example static value, replace as needed)
                        "Pending"      # Initial status
                    )
                    self.tree.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}")

if __name__ == '__main__':
    app = Tk()
    app.title("PC Cleaner")
    Cleaner(app)
    app.mainloop()
