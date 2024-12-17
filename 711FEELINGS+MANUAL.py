import tkinter as tk
from tkinter import messagebox, scrolledtext

def validate_entry(entry):
    if entry.get().strip() == "":
        messagebox.showwarning("Input Error", "This field cannot be empty!")
        return False
    return True

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("711 Feelings: A Mental Health & Productivity Companion")
        self.root.geometry("500x500")
        
        self.home_frame = tk.Frame(root)
        self.home_frame.pack(fill="both", expand=True)
        
        self.create_home_screen()

    def create_home_screen(self):
        # Add header label
        title_label = tk.Label(self.home_frame, text="Welcome to 711 Feelings", font=("Courier New", 14))
        title_label.pack(pady=10)

        task_label = tk.Label(self.home_frame, text="View your tasks or manage your mood", font=("Courier New", 12))
        task_label.pack(pady=10)

        # Button for task management, mood tracking, mindfulness, and exit
        task_button = tk.Button(self.home_frame, text="Manage Tasks", command=self.open_task_management, font=("Courier New", 12))
        task_button.pack(pady=5)

        mood_button = tk.Button(self.home_frame, text="Track Mood", command=self.open_mood_tracker, font=("Courier New", 12))
        mood_button.pack(pady=5)

        mindfulness_button = tk.Button(self.home_frame, text="Mindfulness Exercises", command=self.open_mindfulness, font=("Courier New", 12))
        mindfulness_button.pack(pady=5)

        # Button to toggle the visibility of the User Manual
        self.show_manual_button = tk.Button(self.home_frame, text="Show Manual", command=self.toggle_user_manual, font=("Courier New", 12))
        self.show_manual_button.pack(pady=5)

        # Create the Text widget for the User Manual (initially hidden)
        self.manual_text = tk.Text(self.home_frame, wrap=tk.WORD, width=60, height=15, font=("Courier New", 10))
        self.manual_text.insert(tk.INSERT, """
        **User Manual: 711 Feelings - A Mental Health & Productivity Companion**

        **1. Introduction**
        Welcome to 711 Feelings – a simple and effective tool designed to help you manage your tasks, track your mood, and practice mindfulness. The application is built using Python and Tkinter and provides a user-friendly interface to help you stay organized and maintain a balanced mental state.

        **2. Requirements**
        To run the application, you will need:
        - Python 3.x installed on your machine.
        - Tkinter library (usually pre-installed with Python).

        **3. Running the Application**
        1. Download the source code (`.py` file).
        2. Open a terminal or command prompt.
        3. Navigate to the folder where the file is saved.
        4. Run the application using the command:
           python filename.py
        5. The application window will open, and you will be presented with the main dashboard.

        **4. Application Overview**
        The 711 Feelings application is divided into four main sections:
        - Home Screen: The starting point of the application where you can access all the features.
        - Task Management: A section where you can view and manage your tasks.
        - Mood Tracker: A feature to track your mood on a scale of 1-10.
        - Mindfulness Exercises: A section for practicing mindfulness, including breathing exercises and meditation.

        **5. Navigating the Application**
        On the Home Screen, you can click the buttons to navigate to different sections:
        - Manage Tasks: Opens the Task Management screen.
        - Track Mood: Opens the Mood Tracker screen.
        - Mindfulness Exercises: Opens the Mindfulness Exercises screen.
        - Exit: Closes the application.

        **6. Features Overview**
        - Adding a Task
        - Tracking Your Mood
        - Practicing Mindfulness
        - Input Validation
        - Exiting the Application

        **7. Troubleshooting**
        - Application Not Responding
        - Errors when Adding a Task
        - Mood Rating Not Updating

        **8. Conclusion**
        Thank you for using 711 Feelings. We hope this application helps you stay organized and manage your mental well-being with ease. If you have any feedback or suggestions, feel free to reach out!
        """)

        # Make the Text widget read-only
        self.manual_text.config(state=tk.DISABLED)

        # Initially hide the manual text
        self.manual_text.pack_forget()

    def toggle_user_manual(self):
        # Toggle visibility of the manual text
        if self.manual_text.winfo_ismapped():  # Check if the manual is currently visible
            self.manual_text.pack_forget()   # Hide it
            self.show_manual_button.config(text="Show Manual")  # Change button text to "Show Manual"
        else:
            self.manual_text.pack(pady=10)   # Show the manual
            self.show_manual_button.config(text="Hide Manual")  # Change button text to "Hide Manual"

    def open_task_management(self):
        task_frame = TaskManagement(self.root, self)
        self.show_frame(task_frame.frame)

    def open_mood_tracker(self):
        mood_frame = MoodTracker(self.root, self)
        self.show_frame(mood_frame.frame)

    def open_mindfulness(self):
        mindfulness_frame = Mindfulness(self.root, self)
        self.show_frame(mindfulness_frame.frame)

    def show_frame(self, frame):
        frame.tkraise()

class TaskManagement:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)
        
        self.create_task_management_screen()

    def create_task_management_screen(self):
        task_label = tk.Label(self.frame, text="Task Management", font=("Courier New", 14))
        task_label.pack(pady=10)
        
        task_name_label = tk.Label(self.frame, text="Task Name:", font=("Courier New", 12))
        task_name_label.pack()
        self.task_name_entry = tk.Entry(self.frame, font=("Courier New", 12))
        self.task_name_entry.pack(pady=5)
        
        add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task, font=("Courier New", 12))
        add_task_button.pack(pady=5)
        
        back_button = tk.Button(self.frame, text="Return Home", command=self.app.show_frame(self.app.home_frame), font=("Courier New", 12))
        back_button.pack(pady=5)

    def add_task(self):
        if validate_entry(self.task_name_entry):
            task_name = self.task_name_entry.get()
            messagebox.showinfo("Task Added", f"Task '{task_name}' has been added.")
            self.task_name_entry.delete(0, tk.END)

class MoodTracker:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        self.create_mood_tracker_screen()

    def create_mood_tracker_screen(self):
        mood_label = tk.Label(self.frame, text="Mood Tracker", font=("Courier New", 14))
        mood_label.pack(pady=10)

        mood_slider_label = tk.Label(self.frame, text="Rate your mood (1-10):", font=("Courier New", 12))
        mood_slider_label.pack()
        self.mood_slider = tk.Scale(self.frame, from_=1, to=10, orient="horizontal")
        self.mood_slider.pack(pady=5)

        save_mood_button = tk.Button(self.frame, text="Save Mood", command=self.save_mood, font=("Courier New", 12))
        save_mood_button.pack(pady=5)

        back_button = tk.Button(self.frame, text="Return Home", command=self.app.show_frame(self.app.home_frame), font=("Courier New", 12))
        back_button.pack(pady=5)

    def save_mood(self):
        mood = self.mood_slider.get()
        messagebox.showinfo("Mood Saved", f"Your mood is rated: {mood}/10")

class Mindfulness:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        self.create_mindfulness_screen()

    def create_mindfulness_screen(self):
        mindfulness_label = tk.Label(self.frame, text="Mindfulness Exercises", font=("Courier New", 14))
        mindfulness_label.pack(pady=10)

        breathing_button = tk.Button(self.frame, text="Begin Breathing Exercise", command=self.start_breathing, font=("Courier New",12))
        breathing_button.pack(pady=5)

        meditation_button = tk.Button(self.frame, text="Begin Meditation", command=self.start_meditation, font=("Courier New", 12))
        meditation_button.pack(pady=5)

        back_button = tk.Button(self.frame, text="Return Home", command=self.app.show_frame(self.app.home_frame), font=("Courier New", 12))
        back_button.pack(pady=5)

    def start_breathing(self):
        messagebox.showinfo("Breathing Exercise", "Take a deep breath in... hold... and breathe out...")

    def start_meditation(self):
        messagebox.showinfo("Meditation Exercise", "Sit back and be still. Focus on your breathing...")

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
