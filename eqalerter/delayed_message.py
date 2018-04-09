from base_message import BaseMessage

class DelayedMessage(BaseMessage):

    def __init__(self, timeout, message, title):
        self.message = message
        self.title = title
        self.timeout = timeout
        self.command = 'urxvt -iconic -geometry 15x1 -bg red -fg white -title ' + title + ' -e python stop_watch.py ' + str(timeout) + ' "' + message + '" 1'
