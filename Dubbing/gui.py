import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from irc_a_v12 import connect_to_twitch
import os
import threading

# Load .env file
load_dotenv()

def run_login_app():
    # Function to handle login
    def handle_login(name, password):
        if not name or not password:
            messagebox.showerror("Error", "Please enter both name and password.")
            return
        
        # Print the name and password to the terminal
        print(f"Name: {name}")
        print(f"Password: {password}")
        threading.Thread(target=connect_to_twitch, args=(name, password)).start()


        login_window.destroy()
        show_greeting_window(name)

    # Function to handle login using .env file
    def handle_env_login():
        name = os.getenv("CHANNEL")
        password = os.getenv("OAUTH")
        
        if not name or not password:
            messagebox.showerror("Error", ".env file is missing or incomplete.")
            return
        
        # Print the name and password to the terminal
        print(f"Name: {name}")
        print(f"Password: {password}")
        threading.Thread(target=connect_to_twitch, args=(name, password)).start()
        
        login_window.destroy()
        show_greeting_window(name)

    # Function to show greeting window
    def show_greeting_window(name):
        greeting_window = tk.Tk()
        greeting_window.title("Greeting Window")
        greeting_window.geometry("400x300")  # Set the size of the greeting window

        # Function to handle closing of the greeting window
        def on_greeting_window_close():
            greeting_window.destroy()
            root.quit()

        greeting_window.protocol("WM_DELETE_WINDOW", on_greeting_window_close)
        
        greeting_label = tk.Label(greeting_window, text=f"Hello {name}!", font=("Helvetica", 18))
        greeting_label.pack(pady=20)
        
        greeting_window.mainloop()

    # Function to handle closing of the login window
    def on_login_window_close():
        login_window.destroy()
        

    # Create root window to manage the entire application lifecycle
    root = tk.Tk()
    root.withdraw()  # Hide the root window as it's not needed

    # Create login window
    login_window = tk.Toplevel(root)
    login_window.title("Login Window")
    login_window.geometry("400x300")  # Set the size of the login window

    # Bind the close event to the login window
    login_window.protocol("WM_DELETE_WINDOW", on_login_window_close)

    # Name label and entry
    name_label = tk.Label(login_window, text="Name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(login_window)
    name_entry.pack(pady=5)

    # Password label and entry
    password_label = tk.Label(login_window, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    # Login button
    login_button = tk.Button(login_window, text="Login", command=lambda: handle_login(name_entry.get(), password_entry.get()))
    login_button.pack(pady=10)

    # Login with .env button
    env_login_button = tk.Button(login_window, text="Login with .env", command=handle_env_login)
    env_login_button.pack(pady=5)

    root.mainloop()

