import subprocess
import shlex

class BaseMessage:

    def run(self):
        subprocess.Popen(shlex.split(self.command), close_fds=True)
