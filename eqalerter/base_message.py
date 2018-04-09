class BaseMessage:

    def run(self):
        subprocess.Popen(self.command, close_fds=True)
