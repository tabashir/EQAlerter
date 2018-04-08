from BaseMessage import *
from AudioMessage import *
from VisualMessage import *

class MultiChannelMessage(BaseMessage):

    def __init__(self, message, eq_folder='/path/to/EQ/'):
        self.message = message

    def run(self):
        AudioMessage(message, eq_folder).run()
        VisualMessage(message, eq_folder).run()

