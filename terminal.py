import os

class terminal:
    def __init__(self):
        self.cwd = os.getcwd()

    def execute(self, command):
        parts = command.strip().split()
        if not parts:
            return ""

        cmd = parts[0]
        args = parts[1:]

        if cmd == "exit":
            return "exit"  # signal to quit

        elif cmd == "cd":
            if not args:
                return "Usage: cd [path]"
            try:
                os.chdir(args[0])
                self.cwd = os.getcwd()
            except Exception as e:
                return f"cd error: {e}"
            return ""

        elif cmd == "ls":
            try:
                return "\n".join(os.listdir(self.cwd))
            except Exception as e:
                return f"ls error: {e}"

        elif cmd == "makedir":
            if not args:
                return "Usage: makedir [dirname]"
            try:
                os.mkdir(args[0])
                return f"Directory '{args[0]}' created."
            except Exception as e:
                return f"makedir error: {e}"

        else:
            return f"Unknown command: {cmd}"
