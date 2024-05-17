import tkinter as tk
from tkinter import messagebox
from irc_a_v12 import connect_to_twitch
import threading

def run_login_app():
    def on_submit():
        # Retrieve user inputs
        oauth = oauth_var.get()
        nickname = nickname_var.get()

        print(f"Logged in user: {nickname} and {oauth}")

        # Store the inputs in global variables
        global full_oauth, full_nickname
        full_oauth = oauth
        full_nickname = nickname

        # Display a success message
        messagebox.showinfo("Login Successful", "You are logged in.")

        # Start the Twitch connection in a new thread
        threading.Thread(target=connect_to_twitch, args=(nickname, oauth)).start()

        # Close the login window and open the status window
        root.destroy()
        display_window()

    def display_window():
        # Create a new window to display connection status
        new_window = tk.Tk()
        new_window.title("Status")
        new_window.geometry("400x200")

        # Display the nickname and connection status
        tk.Label(new_window, text=f"Hello, {full_nickname}", font=("Arial", 16)).pack(pady=20)
        tk.Label(new_window, text="Connected to the server", font=("Arial", 16)).pack(pady=20)

        new_window.mainloop()

    def information():
        # Return the stored oauth and nickname
        return full_oauth, full_nickname

    # Initialize the main window
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x200")

    # Define variables to store user inputs
    oauth_var = tk.StringVar()
    nickname_var = tk.StringVar()

    # Create and place the widgets for user input
    tk.Label(root, text="Oauth: ").pack(pady=(20, 0))
    oauth_entry = tk.Entry(root, textvariable=oauth_var)
    oauth_entry.pack()

    tk.Label(root, text="Nickname: ").pack(pady=(10, 0))
    nickname_entry = tk.Entry(root, textvariable=nickname_var)
    nickname_entry.pack()

    # Create and place the submit button
    submit_button = tk.Button(root, text="Log In", command=on_submit)
    submit_button.pack(pady=20)

    root.mainloop()

