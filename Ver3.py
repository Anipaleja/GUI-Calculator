import tkinter as tk
from tkinter import ttk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Scientific Calculator")
        self.geometry("400x600")
        self.configure(bg="#1e1e1e")
        self.expression = ""
        self.history = []

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Entry box
        self.entry = ttk.Entry(self, font=("Segoe UI", 24), justify="right")
        self.entry.pack(fill="x", padx=10, pady=10, ipady=10)
        self.entry.focus()

        # Style for dark mode
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TButton",
                        font=("Segoe UI", 14),
                        padding=10,
                        background="#2e2e2e",
                        foreground="white",
                        borderwidth=1)
        style.map("TButton", background=[("active", "#3e3e3e")])

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(padx=10, pady=5)

        buttons = [
            ["7", "8", "9", "/", "sin"],
            ["4", "5", "6", "*", "cos"],
            ["1", "2", "3", "-", "tan"],
            ["0", ".", "(", ")", "+"],
            ["√", "log", "ln", "^", "="],
            ["π", "e", "C", "⌫", "Hist"]
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                ttk.Button(button_frame, text=char, width=5, command=lambda ch=char: self.on_button_click(ch)).grid(row=r, column=c, padx=2, pady=2)

        # History window
        self.history_box = tk.Text(self, height=8, font=("Segoe UI", 12), bg="#2e2e2e", fg="white", state="disabled")
        self.history_box.pack(fill="both", expand=True, padx=10, pady=10)

    def bind_keys(self):
        self.bind("<Return>", lambda e: self.evaluate())
        self.bind("<BackSpace>", lambda e: self.on_button_click("⌫"))
        self.bind("<Key>", self.keyboard_input)

    def keyboard_input(self, event):
        if event.char in "0123456789.+-*/()^":
            self.entry.insert("end", event.char)

    def on_button_click(self, char):
        if char == "=":
            self.evaluate()
        elif char == "C":
            self.entry.delete(0, tk.END)
        elif char == "⌫":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        elif char == "Hist":
            self.toggle_history()
        elif char == "π":
            self.entry.insert(tk.END, str(math.pi))
        elif char == "e":
            self.entry.insert(tk.END, str(math.e))
        elif char == "√":
            self.entry.insert(tk.END, "math.sqrt(")
        elif char == "log":
            self.entry.insert(tk.END, "math.log10(")
        elif char == "ln":
            self.entry.insert(tk.END, "math.log(")
        elif char == "sin":
            self.entry.insert(tk.END, "math.sin(")
        elif char == "cos":
            self.entry.insert(tk.END, "math.cos(")
        elif char == "tan":
            self.entry.insert(tk.END, "math.tan(")
        elif char == "^":
            self.entry.insert(tk.END, "**")
        else:
            self.entry.insert(tk.END, char)

    def evaluate(self):
        try:
            expression = self.entry.get()
            result = eval(expression, {"math": math})
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            self.add_to_history(expression, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def add_to_history(self, expr, result):
        self.history.append(f"{expr} = {result}")
        self.history_box.config(state="normal")
        self.history_box.insert(tk.END, f"{expr} = {result}\n")
        self.history_box.see(tk.END)
        self.history_box.config(state="disabled")

    def toggle_history(self):
        if self.history_box.winfo_viewable():
            self.history_box.pack_forget()
        else:
            self.history_box.pack(fill="both", expand=True, padx=10, pady=10)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
