import tkinter as tk;


LIGHT_GRAY = "#F5F5F5"
class Calculator:
    def __init__(self):
        self.window = tk.Tk();
        self.window.geometry("375x667")
        self.window.resizable(0,0);
        self.window.title("Calculator")

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_frame(self):
        frame = tk.Frame(self.window,height

    def run(self):
        self.window.mainloop()

    if __name__ == "__main__":
        calc = Calculator()
        calc.run()

