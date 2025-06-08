import os
import subprocess
import platform

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

        elif cmd == "rmdir":
            if not args:
                return "Usage: rmdir [dirname]"
            try:
                os.rmdir(args[0])
                return f"Directory '{args[0]}' removed."
            except Exception as e:
                return f"rmdir error: {e}"

        elif cmd == "run":
            if not args:
                return "Usage: run [executable]"
            try:
                result = subprocess.run(args, cwd=self.cwd, capture_output=True, text=True, shell=True)
                return result.stdout or result.stderr
            except Exception as e:
                return f"run error: {e}"

        elif cmd == "clear":
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            return ""

        elif cmd == "rename":
            if len(args) != 2:
                return "Usage: rename [old_name] [new_name]"
            try:
                os.rename(args[0], args[1])
                return f"Renamed '{args[0]}' to '{args[1]}'."
            except Exception as e:
                return f"rename error: {e}"

        elif cmd == "mikel":
            return "KONTOL"

        else:
            return f"Unknown command: {cmd}"
