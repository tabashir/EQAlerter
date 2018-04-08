

class SimpleMessage:

    def __init__(self, message):
        self.message = message


class BackgroundTask:

    def __init__(self, timeout, message, title):
        self.message = message
        self.title = title
        self.timeout = timeout

