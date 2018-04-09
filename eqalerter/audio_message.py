from base_message import BaseMessage

class AudioMessage(BaseMessage):

    def __init__(self, message):
        self.message = message
        base_command = 'flite -voice slt -t '
        self.command = base_command + '"' + message + '"'
