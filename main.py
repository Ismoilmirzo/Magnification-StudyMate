import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class StudyMateApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("StudyMate")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        

        self.create_menu()
        self.create_description_page()
        self.create_magnification_calculator_page()
        self.create_organisation_page()
        
        self.show_description_page()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Create the Description menu
        description_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Description", menu=description_menu)
        description_menu.add_command(label="Magnification", command=self.show_description_page)

        # Create the Magnification Calculator menu
        calculator_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Magnification Calculator", menu=calculator_menu)
        calculator_menu.add_command(label="Calculator", command=self.show_calculator_page)

        # Create the Our Organisation menu
        organisation_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Our Organisation", menu=organisation_menu)
        organisation_menu.add_command(label="Our Projects", command=self.open_website)

    def create_description_page(self):
        self.description_frame = ttk.Frame(self.root)
        self.description_frame.place(relwidth=1, relheight=1)

        description_text = "App aims to helps students to learn magnification in biology A-Levels easily"
        description_label = ttk.Label(self.description_frame, text=description_text)
        description_label.pack(pady=10)

        table_frame = ttk.Frame(self.description_frame)
        table_frame.pack()

        ttk.Label(table_frame, text="Measure").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(table_frame, text="Scale").grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(table_frame, text="1 Millimetre").grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(table_frame, text="1/1000 of a Metre").grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(table_frame, text="1 Micrometre").grid(row=2, column=0, padx=10, pady=5)
        ttk.Label(table_frame, text="1/1000000 of a Metre").grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(table_frame, text="1 Nanometre").grid(row=3, column=0, padx=10, pady=5)
        ttk.Label(table_frame, text="1/1000000000 of a Metre").grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(table_frame, text="1 Picometre").grid(row=4, column=0, padx=10, pady=5)
        ttk.Label(table_frame, text="1/1000000000000 of a Metre").grid(row=4, column=1, padx=10, pady=5)


        formula_text = "Magnification Formula: Measured size = Magnification × Actual size"
        formula_description_label = ttk.Label(self.description_frame, text=formula_text)
        formula_description_label.pack(pady=10)

    def create_magnification_calculator_page(self):
        self.calculator_frame = ttk.Frame(self.root)
        self.calculator_frame.place(relwidth=1, relheight=1)

        ttk.Label(self.calculator_frame, text="Magnification Calculator", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.magnification_label = ttk.Label(self.calculator_frame, text="Magnification:")
        self.magnification_label.pack()

        self.magnification_entry = ttk.Entry(self.calculator_frame)
        self.magnification_entry.pack()

        self.actual_size_label = ttk.Label(self.calculator_frame, text="Actual Size (mm):")
        self.actual_size_label.pack()

        self.actual_size_entry = ttk.Entry(self.calculator_frame)
        self.actual_size_entry.pack()

        self.measured_size_label = ttk.Label(self.calculator_frame, text="Measured Size (mm):")
        self.measured_size_label.pack()

        self.measured_size_entry = ttk.Entry(self.calculator_frame)
        self.measured_size_entry.pack()

        calculate_button = ttk.Button(self.calculator_frame, text="Calculate", command=self.calculate_magnification)
        calculate_button.pack(pady=10)

        self.result_label = ttk.Label(self.calculator_frame, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def create_organisation_page(self):
        self.organisation_frame = ttk.Frame(self.root)
        self.organisation_frame.place(relwidth=1, relheight=1)

        ttk.Label(self.organisation_frame, text="About Our Organisation", font=("Helvetica", 16, "bold")).pack(pady=10)
        # Add more content or design elements to the Organisation page as needed
        ...

    def show_description_page(self):
        self.description_frame.tkraise()

    def show_calculator_page(self):
        self.calculator_frame.tkraise()

    def show_organisation_page(self):
        self.organisation_frame.tkraise()

    def calculate_magnification(self):
        try:
            magnification = float(self.magnification_entry.get() or 0)
            actual_size = float(self.actual_size_entry.get() or 0)
            measured_size = float(self.measured_size_entry.get() or 0)

            if not magnification:
                magnification = measured_size / actual_size
                self.magnification_entry.delete(0, tk.END)
                self.magnification_entry.insert(0, str(round(magnification, 2)))
            elif not actual_size:
                actual_size = measured_size / magnification
                self.actual_size_entry.delete(0, tk.END)
                self.actual_size_entry.insert(0, str(round(actual_size, 2)))
            elif not measured_size:
                measured_size = actual_size * magnification
                self.measured_size_entry.delete(0, tk.END)
                self.measured_size_entry.insert(0, str(round(measured_size, 2)))

            self.result_label.config(text="Calculation Successful", foreground="green")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numeric values.", foreground="red")

    def open_website(self):
        import webbrowser
        webbrowser.open("https://matestudy.netlify.app/")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    study_mate_app = StudyMateApp()
    study_mate_app.run()
