import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to the database
conn = sqlite3.connect('Quiz_Bowl_Database.db')
cursor = conn.cursor()

# Quiz Window class
class QuizWindow:
    def __init__(self, course_name):
        self.course_name = course_name
        self.questions = self.get_questions(course_name)
        self.question_index = 0
        self.score = 0
        self.quiz_window = tk.Tk()  # Create a new main window for the quiz
        self.quiz_window.title(f"{self.course_name} Quiz")
        self.quiz_window.geometry("400x300")
        self.var = tk.StringVar()  # Initialize StringVar for radio button selection
        self.setup_window()
        self.load_question()

    # Function to get all questions for the selected course
    def get_questions(self, table_name):
        cursor.execute(f"SELECT question, answer, option1, option2, option3, option4 FROM {table_name}")
        return cursor.fetchall()

    # Setup the quiz window interface
    def setup_window(self):
        self.question_label = tk.Label(self.quiz_window, text="", wraplength=350, font=("Arial", 12), justify="left")
        self.question_label.pack(pady=10)

        # Clear selection each time setup_window is called
        self.var.set("")  # Ensure no default selection on the first load

        # Create radio buttons for answer options
        self.radio_buttons = [
            tk.Radiobutton(self.quiz_window, text="", variable=self.var, font=("Arial", 10), value="", command=self.highlight_selection)
            for _ in range(4)
        ]
        for radio_button in self.radio_buttons:
            radio_button.pack(anchor="w", padx=20)

        # Button to go to the next question
        self.next_button = tk.Button(self.quiz_window, text="Next Question", command=self.check_answer)
        self.next_button.pack(pady=20)

    # Function to load the current question and display answer options
    def load_question(self):
        if self.question_index < len(self.questions):
            question, answer, option1, option2, option3, option4 = self.questions[self.question_index]
            self.question_label.config(text=question)
            self.correct_answer = answer
            self.var.set("")  # Clear selection each time a new question loads

            # Set text and value of each radio button to display answer options
            radio_options = [option1, option2, option3, option4]
            for i, radio_button in enumerate(self.radio_buttons):
                radio_button.config(text=radio_options[i], value=radio_options[i])
                radio_button.deselect()  # Ensure no radio button is selected by default
                radio_button.config(bg="SystemButtonFace")  # Reset background color
        else:
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(self.questions)}")
            self.quiz_window.destroy()

    # Function to highlight selected answer
    def highlight_selection(self):
        for radio_button in self.radio_buttons:
            if radio_button.cget("value") == self.var.get():
                radio_button.config(bg="lightblue")
            else:
                radio_button.config(bg="SystemButtonFace")

    # Function to check answer and load next question
    def check_answer(self):
        selected_answer = self.var.get()
        if selected_answer == self.correct_answer:
            self.score += 1
            self.show_feedback_popup("Correct!", "✔️", "green")
        else:
            self.show_feedback_popup("Incorrect", "❌", "red")
        self.question_index += 1
        self.load_question()

    # Function to show feedback popup without minimize, maximize, or close buttons
    def show_feedback_popup(self, message, symbol, color):
        # Create the popup window as a top-level window
        popup = tk.Toplevel(self.quiz_window)
        popup.geometry("150x100")
        
        # Remove window decorations (no close, minimize, or maximize buttons)
        popup.overrideredirect(True)

        # Get screen dimensions to center the popup
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        popup_x = (screen_width // 2) - 75  # Center horizontally
        popup_y = (screen_height // 2) - 50  # Center vertically
        popup.geometry(f"150x100+{popup_x}+{popup_y}")

        # Add border by placing a frame with a background color
        border_frame = tk.Frame(popup, bg="black", padx=3, pady=3)
        border_frame.pack(fill="both", expand=True)

        # Inner frame for actual content, with padding for border effect
        inner_frame = tk.Frame(border_frame, bg="white")
        inner_frame.pack(fill="both", expand=True, padx=3, pady=3)

        # Feedback symbol and message
        label = tk.Label(inner_frame, text=symbol, font=("Arial", 30), fg=color, bg="white")
        label.pack(pady=10)
        text_label = tk.Label(inner_frame, text=message, font=("Arial", 12), bg="white")
        text_label.pack()

        # Automatically close the popup after a short delay
        popup.after(1000, popup.destroy)

# Main application window for selecting a course
def start_quiz():
    selected_course = course_var.get()
    if selected_course:
        root.destroy()  # Close the main window
        QuizWindow(selected_course)  # Open the quiz window
    else:
        messagebox.showwarning("Select Course", "Please select a course to start the quiz.")

# Setup main window for course selection
root = tk.Tk()
root.title("Quiz Bowl")
root.geometry("300x200")

# Label and dropdown for selecting a course
tk.Label(root, text="Select a Course", font=("Arial", 14)).pack(pady=10)
course_var = tk.StringVar()
courses = ["DS_3850", "DS_4220", "DS_4210", "MKT_3400", "HIST_1310"]
course_menu = ttk.Combobox(root, textvariable=course_var, values=courses, state="readonly")
course_menu.pack(pady=10)

# Button to start the quiz
start_button = tk.Button(root, text="Start Quiz Now", command=start_quiz)
start_button.pack(pady=20)

# Run the main loop
root.mainloop()

# Close the database connection when done
conn.close()