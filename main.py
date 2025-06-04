import tkinter as tk
from terminal import terminal

class TerminalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chimken Terminal")

        self.core = terminal()
        self.prompt = f"{self.core.cwd} > "

        self.text = tk.Text(root, bg="black", fg="white", insertbackground="white",
                            font=("Helvetica", 12), wrap=tk.WORD)
        self.text.pack(expand=True, fill=tk.BOTH)
        self.text.insert(tk.END, f"Chimken Terminal [ketik 'exit' untuk keluar]\n{self.prompt}")
        self.text.focus()

        self.text.bind("<Return>", self.on_enter)
        self.text.bind("<Key>", self.block_editing, add="+")

        self.cmd_start = self.text.index("insert")

    def block_editing(self, event):
        if self.text.compare("insert", "<", self.cmd_start):
            return "break"

    def on_enter(self, event):
        line = self.get_current_command().strip()
        self.text.insert(tk.END, "\n")
        result = self.core.execute(line)

        if result == "exit":
            self.root.quit()
            return "break"

        if result:
            self.text.insert(tk.END, result + "\n")

        self.prompt = f"{self.core.cwd} > "
        self.text.insert(tk.END, self.prompt)
        self.cmd_start = self.text.index("insert")
        return "break"

    def get_current_command(self):
        return self.text.get(self.cmd_start, tk.END).strip()

def main():
    root = tk.Tk()
    terminal = TerminalGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
