# firebase_config.py

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
