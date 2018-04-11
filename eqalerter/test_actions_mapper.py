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

    def test_message_action_instantiation(self):
        unit = ActionsMapper("test_actions_basic.yml")
        item = unit.actions['MARNEK1']
        self.assertEqual('Marnek enters the realm of the dead', item.expect)
        self.assertEqual('Marnek is in skeleton form', item.message)

    def test_message_instantiation_with_ignores(self):
        unit = ActionsMapper("test_actions_with_ignores.yml")
        item = unit.actions['TELL']
        self.assertEqual('tells you,', item.expect)
        self.assertEqual('Incoming Tell', item.message)
        self.assertEqual(["That'll be", 'Attacking'], item.ignore)

    def test_ignore_defaults_to_empty_array(self):
        unit = ActionsMapper("test_actions_basic.yml")
        item = unit.actions['MARNEK1']
        self.assertEqual([], item.ignore)

    def test_timer_instantiation(self):
        unit = ActionsMapper("test_actions_tasks.yml")
        item = unit.actions['MEZ']
        self.assertEqual('has been mesmerized', item.expect)
        self.assertEqual('Mezmerize', item.title)
        self.assertEqual('Mesmerize warning', item.message)
        self.assertEqual(19, item.time)

    def test_basic_instantiation_defaults(self):
        unit = ActionsMapper("test_actions_basic.yml")
        item = unit.actions['MARNEK1']
        self.assertEqual([], item.ignore)

    def test_timer_instantiation_defaults(self):
        unit = ActionsMapper("test_actions_tasks.yml")
        item = unit.actions['FASCINATE']
        self.assertEqual('has been fascinated', item.expect)
        self.assertEqual([], item.ignore)
        self.assertEqual('Timer', item.title)
        self.assertEqual(31, item.time)

    def test_timer_instantiation_with_ignores(self):
        unit = ActionsMapper("test_actions_tasks_with_ignores.yml")
        item = unit.actions['MEZ']
        self.assertEqual('action with ignore', item.expect)
        self.assertEqual('action with ignore message', item.message)
        self.assertEqual([ "by somebody else", "another ignore" ], item.ignore)


if __name__ == '__main__':
    unittest.main()
