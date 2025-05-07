import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 GPA Tracker")
        self.root.geometry("700x600")

        self.semesters = {}  # {Semester: [(Subject, Marks)]}

        # UI Elements
        self.sem_label = tk.Label(root, text="Semester Name:")
        self.sem_label.pack()
        self.sem_entry = tk.Entry(root)
        self.sem_entry.pack()

        self.sub_label = tk.Label(root, text="Subject Name:")
        self.sub_label.pack()
        self.sub_entry = tk.Entry(root)
        self.sub_entry.pack()

        self.marks_label = tk.Label(root, text="Marks (0-100):")
        self.marks_label.pack()
        self.marks_entry = tk.Entry(root)
        self.marks_entry.pack()

        self.add_button = tk.Button(root, text="Add Subject", command=self.add_subject)
        self.add_button.pack(pady=5)

        self.calc_button = tk.Button(root, text="Calculate GPA", command=self.calculate_gpa)
        self.calc_button.pack(pady=5)

        self.plot_button = tk.Button(root, text="Plot GPA Trend", command=self.plot_gpa)
        self.plot_button.pack(pady=5)

        self.output = tk.Text(root, height=10, width=80)
        self.output.pack(pady=10)

    def add_subject(self):
        semester = self.sem_entry.get()
        subject = self.sub_entry.get()
        try:
            marks = float(self.marks_entry.get())
            if not (0 <= marks <= 100):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid marks between 0-100.")
            return

        if semester not in self.semesters:
            self.semesters[semester] = []
        self.semesters[semester].append((subject, marks))

        messagebox.showinfo("Success", f"Added {subject} to {semester}")
        self.clear_entries()

    def calculate_gpa(self):
        self.output.delete('1.0', tk.END)
        result = ""
        gpa_data = {}
        for semester, subjects in self.semesters.items():
            total_grade_points = 0
            for subject, marks in subjects:
                grade_point = self.get_grade_point(marks)
                total_grade_points += grade_point
            gpa = round(total_grade_points / len(subjects), 2)
            gpa_data[semester] = gpa
            result += f"{semester}: GPA = {gpa}\n"

        self.gpa_data = gpa_data
        self.output.insert(tk.END, result)

    def plot_gpa(self):
        if not hasattr(self, 'gpa_data') or not self.gpa_data:
            messagebox.showinfo("Calculate First", "Please calculate GPA before plotting.")
            return

        fig, ax = plt.subplots()
        semesters = list(self.gpa_data.keys())
        gpas = list(self.gpa_data.values())

        ax.plot(semesters, gpas, marker='o', linestyle='-', color='teal')
        ax.set_xlabel("Semester")
        ax.set_ylabel("GPA")
        ax.set_title("GPA Trend Over Semesters")
        ax.grid(True)

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def get_grade_point(self, marks):
        if marks >= 90: return 10
        elif marks >= 80: return 9
        elif marks >= 70: return 8
        elif marks >= 60: return 7
        elif marks >= 50: return 6
        elif marks >= 40: return 5
        else: return 0

    def clear_entries(self):
        self.sem_entry.delete(0, tk.END)
        self.sub_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()
