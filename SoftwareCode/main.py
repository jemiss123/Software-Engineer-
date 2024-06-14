import tkinter as tk
from user_pages.login import LoginPage
from user_pages.register import RegisterPage
from user_pages.forgotPassword import ForgotPasswordPage
from user_pages.home import HomePage
from user_pages.resetPassword import ResetPasswordPage


class App:
    def __init__(self, root):
        self.shared_data = {}  # Initialize shared_data as a dictionary
        self.root = root
        self.root.title("Call Dr.")
        self.root.geometry("1050x594")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.pages = {}

        self.pages["login"] = LoginPage(self)
        self.pages["register"] = RegisterPage(self)
        self.pages["forgotpassword"] = ForgotPasswordPage(self)
        self.pages["home"] = HomePage(self)
        self.pages["resetpassword"] = ResetPasswordPage(self)

        self.show_page("login")

    def show_page(self, page_name, username=None):
        for page in self.pages.values():
            page.frame.pack_forget()

        if username:
            self.set_shared_data("username", username)

        self.pages[page_name].frame.pack(fill='both', expand=True)

    def add_page(self, page_name, frame):
        self.pages[page_name] = frame

    def set_shared_data(self, key, value):
        self.shared_data[key] = value

    def get_shared_data(self, key):
        return self.shared_data.get(key, None)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
