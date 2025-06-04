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

        elif cmd == "opend":
            if not args:
                return "How to: opend [path]"
            try:
                os.chdir(args[0])
                self.cwd = os.getcwd()
            except Exception as e:
                return f"opend error: {e}"
            return ""

        elif cmd == "lookd":
            try:
                return "\n".join(os.listdir(self.cwd))
            except Exception as e:
                return f"lookd error: {e}"

        elif cmd == "mdirect":
            if not args:
                return "How to: mdirect [dirname]"
            try:
                os.mkdir(args[0])
                return f"Directory '{args[0]}' terbuat."
            except Exception as e:
                return f"mdirect error: {e}"

        else:
            return f"Unknown command: {cmd}"
