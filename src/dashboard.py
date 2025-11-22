from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from .calculation import Calculation

class Dashboard:
    def __init__(self):
        self.root = Tk()
        self.calculate = Calculation()
        self.dash = ttk.Frame(self.root, padding=10)
        self.entry_1, self.entry_2 = self.create_entries()

        # Result label
        self.result_label = ttk.Label(self.dash, text="", font=('Helvetica', 14))

    def create_main(self):
        # Title
        self.root.title('')
        title_label = ttk.Label(self.dash, text="Welcome to Edit Distance Calculation")
        title_label['font'] = ('Helvetica', 24, 'bold')  # Bigger font
        title_label.grid(column=0, row=0, columnspan=2, pady=20)
        # Dashboard Size
        self.root.geometry('800x600')
        # Create all buttons
        self.create_buttons()
        # Text
        (ttk.Label(self.dash, text='Please input two words for the edit distance')
         .grid(column=0, row=1, columnspan=1, pady=0))
        # Dashboard Grid
        self.dash.grid()
        # Run main loop
        self.root.mainloop()

    def create_buttons(self):
        # Exit button
        ttk.Button(self.dash, text='QUIT', command=self.root.destroy).grid(column=2, row=7)
        # Submit Button
        ttk.Button(self.dash, text='Submit', command=self.display_results).grid(column=0, row=7)
        # Clear Button
        ttk.Button(self.dash, text='Clear', command=self.clear_entries).grid(column=1, row=7)
        # Entry boxes
        self.entry_1.grid(column=0, row=3, padx=0, pady=0)
        self.entry_2.grid(column=0, row=4, padx=0, pady=0)

    def create_entries(self):
        # Labels
        ttk.Label(self.dash, text="First Word:").grid(column=0, row=3, sticky=W, pady=5)
        ttk.Label(self.dash, text="Second Word:").grid(column=0, row=4, sticky=W, pady=5)

        # Entry boxes
        entry_1 = ttk.Entry(self.dash, width=30)
        entry_2 = ttk.Entry(self.dash, width=30)

        entry_1.grid(column=1, row=1, padx=0, pady=0)
        entry_2.grid(column=1, row=2, padx=0, pady=0)

        return entry_1, entry_2

    def get_input(self):
        # Get inputs and convert to lowercase
        word_1, word_2 = self.entry_1.get().lower(), self.entry_2.get().lower()

        # Check if either entry is empty
        if not word_1 or not word_2:
            messagebox.showwarning("Input Error", "Both words must be entered!")
            return None, None
        # Check for alphabetical characters only
        if not word_1.isalpha() or not word_2.isalpha():
            messagebox.showwarning("Input Error", "Only alphabetic characters allowed!")
            return None, None

        return word_1, word_2


    def calculate_edit_distance(self):
        word_1, word_2 = self.get_input()
        distance, matrix = self.calculate.calculate_edit_distance(word_1, word_2)
        return distance, matrix, word_1, word_2

    def display_results(self):
        distance, matrix, word_1, word_2 = self.calculate_edit_distance()
        matrix_display = ttk.Label(
            self.dash,
            text=self.calculate.display_matrix(word_1, word_2)
        )
        matrix_display['font'] = ('Courier New', 8)  # Monospace font
        matrix_display.grid(column=0, row=5, columnspan=2, pady=20)

        alignment_display = ttk.Label(
            self.dash,
            text=self.calculate.display_alignment()
        )
        alignment_display['font'] = ('Courier New', 8)
        alignment_display.grid(column=0, row=8, columnspan=2, pady=20)


    def clear_entries(self):
        """Clear the entry boxes and result label"""
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        # self.result_label.config(text="")