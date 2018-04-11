from delayed_message import DelayedMessage
from multi_channel_message import MultiChannelMessage
from base_message import BaseMessage
from audio_message import AudioMessage
from visual_message import VisualMessage

class MessageGenerator:

    def __init__(self, eq_home, character_name, actions):
        self.eq_home = eq_home
        self.character_name = character_name
        self.actions = actions
        # print('DEBUG_INIT: ' + str(self.actions))

    def action_for(self, line):
        for name, action  in self.actions.items():
            named_line = action.expect.format(CHARACTER=self.character_name)
            if named_line in line:
                for ignore_line in action.ignore:
                    if ignore_line in line:
                        return

                if hasattr(action, 'time'):
                    return DelayedMessage(action.time, action.message, action.title)

                return MultiChannelMessage(action.message, self.eq_home)
