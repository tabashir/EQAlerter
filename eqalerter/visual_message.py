from base_message import BaseMessage

class VisualMessage(BaseMessage):

    def __init__(self, message, eq_folder='/path/to/EQ/'):
        self.message = message
        base_command = 'notify-send --urgency low --expire-time=1000 --icon='+eq_folder+'EverQuest.ico '
        self.command = base_command + '"' + message + '"'

