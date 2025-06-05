# This file is for GUI based experience
# 'gui.py' is the GUI file, 'logic.py' is the logic for running the program
# Run this file in the terminal or via Python Run command to launch the GUI. 
# "python gui.py" to run.

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from logic import run_commit_script
import threading

# Class for GUI
class GitCommitGUI:
    #Define root window (master window that all widgets are underr)
    # Self is the current instance of this program
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Commit Automator")
        self.entries = {}

        #Fields for user input to pass to logic.py
        #These are placeholders which can be changed when running the GUI
        fields = [
            ("GitHub Repo URL", "https://github.com/YOUR_USERNAME/github-activity.git"),
            ("Local Repo Name", "temp-repo"),
            ("GitHub Username", "YOUR_USERNAME"),
            ("Email", "your.email@example.com"),
            ("Git Branch", "main"),  # NEW
            ("Days Back", "365"),
            ("Max Commits Per Day", "3"),
        ]

        # Pass placeholder field data to tkinter fields
        for label_text, default in fields:
            frame = ttk.Frame(root)
            frame.pack(pady=4, padx=10, fill="x")

            label = ttk.Label(frame, text=label_text, width=25)
            label.pack(side="left")

            var = tk.StringVar(value=default)
            entry = ttk.Entry(frame, textvariable=var, width=40)
            entry.pack(side="right", fill="x", expand=True)

            self.entries[label_text] = var

        # Run button for running the program
        self.run_button = ttk.Button(root, text="Run Script", command=self.run_script)
        self.run_button.pack(pady=10)

        # Log window to track program progress & troubleshooting (good luck lol)
        log_frame = ttk.Frame(root)
        log_frame.pack(padx=10, pady=(5, 15), fill="both", expand=True)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, wrap=tk.WORD, state="disabled")
        self.log_text.pack(fill="both", expand=True)

    # 
    def append_log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")
        self.root.update_idletasks()

    # Disables run button when program is running
    def run_script(self):
        self.run_button.config(state="disabled")
        self.append_log("=== Starting Git Automation ===")

        # Threading keeps the GUI responsive by handing logic process to background thread to keep the GUI responseive/live
        # Def had to look up how to do this lol
        # But this passes the run_commit_script to that background thread process
        def thread_function():
            run_commit_script(
                repo_url=self.entries["GitHub Repo URL"].get(),
                local_repo=self.entries["Local Repo Name"].get(),
                username=self.entries["GitHub Username"].get(),
                email=self.entries["Email"].get(),
                days_back=self.entries["Days Back"].get(),
                max_commits=self.entries["Max Commits Per Day"].get(),
                branch=self.entries["Git Branch"].get(),
                status_callback=self.append_log
            )
            self.run_button.config(state="normal")

        threading.Thread(target=thread_function, daemon=True).start()

# Executes the GUI initialization and loops it to keep it reponsive and live
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x600")
    gui = GitCommitGUI(root)
    root.mainloop()
