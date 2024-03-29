import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")

        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        entry = tk.Entry(self, textvariable=self.result, font=("Arial", 24), bd=10)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and arithmetic operations
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, text):
        if text == "=":
            try:
                expression = self.result.get()
                result = eval(expression)
                self.result.set(result)
            except:
                self.result.set("Error")
        else:
            current_text = self.result.get()
            new_text = current_text + text
            self.result.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
