#!/usr/bin/env python

import unittest
from config import *
from delayed_message import DelayedMessage
from multi_channel_message import MultiChannelMessage
from base_message import BaseMessage
from audio_message import AudioMessage
from visual_message import VisualMessage
from actions_mapper import ActionsMapper

class TestActionsMapper(unittest.TestCase):

    def test_loading(self):
        unit = ActionsMapper("test_actions_basic.yml")
        self.assertEqual(6, len(unit.actions))

    def test_basic_action_instantiation(self):
        unit = ActionsMapper("test_actions_basic.yml")
        self.assertEqual('Marnek enters the realm of the dead', unit.actions[0].expect)
        self.assertEqual('Marnek is in skeleton form', unit.actions[0].message)

    def test_action_instantiation_with_ignores(self):
        unit = ActionsMapper("test_actions_with_ignores.yml")
        self.assertEqual('tells you,', unit.actions[0].expect)
        self.assertEqual('Incoming Tell', unit.actions[0].message)
        self.assertEqual(["That'll be", 'Attacking'], unit.actions[0].ignore)

if __name__ == '__main__':
    unittest.main()
