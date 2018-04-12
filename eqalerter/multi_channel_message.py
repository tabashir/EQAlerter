from base_message import BaseMessage
from audio_message import AudioMessage
from visual_message import VisualMessage

class MultiChannelMessage(BaseMessage):

    def __init__(self, message, eq_folder):
        self.message = message
        self.eq_folder = eq_folder

    def run(self):
        AudioMessage(self.message).run()
        VisualMessage(self.message, self.eq_folder).run()

