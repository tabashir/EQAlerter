from delayed_message import DelayedMessage
from multi_channel_message import MultiChannelMessage
from base_message import BaseMessage
from audio_message import AudioMessage
from visual_message import VisualMessage

class MessageGenerator:

    def __init__(self, eq_home, character_name, action_list):
        self.eq_home = eq_home
        self.character_name = character_name
        self.action_list = action_list

    def action_for(self, line):
        for action in self.action_list:
            named_line = action['expect'].format(CHARACTER=self.character_name)
            if named_line in line:
                # print('DEBUG: ' + named_line)
                for ignore_line in action.get('ignore', []):
                    if ignore_line in line:
                        return

                if 'task' in action:
                    task = action['task']
                    return DelayedMessage(task['time'], task['message'], task['title'])

                return MultiChannelMessage(action['message'], self.eq_home)
