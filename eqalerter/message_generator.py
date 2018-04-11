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

    def action_for(self, line):
        for name, action  in self.actions:
            print('DEBUG: ' + name + ' EXPECT: ' + action['expect'])
            named_line = action['expect'].format(CHARACTER=self.character_name)
            print('DEBUG: ' + named_line)
            if named_line in line:
                print('DEBUG: ' + named_line)
                for ignore_line in action.get('ignore', []):
                    if ignore_line in line:
                        return

                if 'time' in action:
                    return DelayedMessage(task['time'], task['message'], task['title'])

                return MultiChannelMessage(action['message'], self.eq_home)
