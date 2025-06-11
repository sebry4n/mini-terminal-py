import os
import subprocess
import platform
import webbrowser

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
            return "__clear__"

        elif cmd == "rename":
            if len(args) != 2:
                return "Usage: rename [old_name] [new_name]"
            try:
                os.rename(args[0], args[1])
                return f"Renamed '{args[0]}' to '{args[1]}'."
            except Exception as e:
                return f"rename error: {e}"

        elif cmd == "mikel":
            return "Hartoyo"
        
        elif cmd == "edu":
            return "Nata"
        
        elif cmd == "palel":
            return "papaw"
        
        elif cmd == "buka":
            if not args:
                return "How to : buka [blablabla.urextension]"
            try:
                os.startfile(args[0])
                return f"opened '{args[0]}'."
            except Exception as e:
                return f"buka error: {e}"
            
        elif cmd == "make":
            if not args:
                return "How to : make [blablabla.urxtensuin]"
            try:
                open(args[0], "w").close()
                return f"made '{args[0]}' text."
            except Exception as e:
                return f"buka error: {e}"
            
        elif cmd == "web":
            if not args:
                return "How to : web [url]"
            try:
                webbrowser.open(f"{args[0]}")
                return f"web terbuka '{args[0]}'"
            except Exception as e:
                return f"web error: {e}"
            
        elif cmd == "list":
                return " exit\n opend\n lookd\n mdirect\n rmdir\n run\n clear\n buka\n make\n web\n"

        else:
            return f"Unknown command: {cmd}"
