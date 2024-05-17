import tkinter as tk
from tkinter import messagebox
from irc_a_v12 import connect_to_twitch
import threading


def run_login_app():
    def on_submit():

        oauth = ouath_var.get()
        nickname = nickname_var.get()

        print(f"Logged in user: {nickname} and {oauth}")

        global full_oauth, full_nickname

        full_oauth = oauth
        full_nickname = nickname
        messagebox.showinfo("Loggin Successful", "You are logged in.")

        threading.Thread(target=connect_to_twitch, args=(nickname, oauth)).start()

        root.destroy()
        display_window()

    def display_window():

        new_window = tk.Tk()
        new_window.title("Status")
        new_window.geometry("400x200")

        tk.Label(new_window, text=f"Hello, {full_nickname}", font=("Arial", 16)).pack(
            pady=20
        )

        tk.Label(new_window, text="Connected to the server", font=("Arial", 16)).pack(
            pady=20
        )

        new_window.mainloop()

    def information():
        return full_oauth, full_nickname

    root = tk.Tk()
    root.title("Login")
    root.geometry("400x200")

    ouath_var = tk.StringVar()
    nickname_var = tk.StringVar()

    tk.Label(root, text="Oauth: ").pack(pady=(20, 0))
    oauth_entry = tk.Entry(root, textvariable=ouath_var)
    oauth_entry.pack()

    tk.Label(root, text="Nickname: ").pack(pady=(10, 0))
    nickname_entry = tk.Entry(root, textvariable=nickname_var)
    nickname_entry.pack()

    submit_button = tk.Button(root, text="Log In", command=on_submit)
    submit_button.pack(pady=20)

    root.mainloop()
