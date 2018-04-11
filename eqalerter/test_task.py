#!/usr/bin/env python

import unittest
from config import *
from delayed_message import DelayedMessage
from multi_channel_message import MultiChannelMessage
from base_message import BaseMessage
from audio_message import AudioMessage
from visual_message import VisualMessage

class TestTask(unittest.TestCase):

    def test_simple_message(self):
        unit = AudioMessage("my message")
        self.assertEqual("my message", unit.message)
        self.assertTrue(callable(getattr(unit, 'run')))

    def test_delayed_message(self):
        unit = DelayedMessage(42, "my message description", "msgtitle")
        self.assertEqual("my message description", unit.message)
        self.assertEqual("msgtitle", unit.title)
        self.assertEqual(42, unit.timeout)
        self.assertTrue(callable(getattr(unit, 'run')))

    def test_audio_message_command_line(self):
        unit = AudioMessage("my message")
        expected = 'flite -voice slt -t "my message"'
        self.assertEqual(expected, unit.command)

    def test_visual_message_command_line(self):
        unit = VisualMessage("my message")
        expected = 'notify-send --urgency low --expire-time=1000 --icon=/path/to/EQ/EverQuest.ico "my message"'
        self.assertEqual(expected, unit.command)

    def test_delayed_message_command_line(self):
        unit = DelayedMessage(42, "my message description", "msgtitle")
        expected = 'urxvt -iconic -geometry 15x1 -bg red -fg white -title msgtitle -e python stop_watch.py 42 "my message description" 1'
        self.assertEqual(expected, unit.command)

if __name__ == '__main__':
    unittest.main()
