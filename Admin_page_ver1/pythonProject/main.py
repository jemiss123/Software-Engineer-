# using 'pip install firebase_admin' to install this also, don't forget
# using 'pip install pyrebase' to install pyrebase, if can't download, off ur antivirus to install
# with problem, review this YouTube video (https://www.youtube.com/watch?v=eGCC3Se6QUE)
import pyrebase
import tkinter as tk
import user_pages.login
from user_pages.home import Home


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




if __name__ == "__main__":
    root = tk.Tk()
    home_instance = Home(root)
    app = user_pages.login.Login(root, home_instance)
    root.mainloop()

