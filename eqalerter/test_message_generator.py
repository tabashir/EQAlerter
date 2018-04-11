#!/usr/bin/env python

import unittest
from message_generator import MessageGenerator
from actions_mapper import Action
from actions_mapper import ActionsMapper

IRRELEVANT_CHARACTER = 'nomatter'
ACTIONS_MAP = ActionsMapper("test_action_mapper_data.yml").actions

class TestMessageGenerator(unittest.TestCase):

    def test_unrecognised_line_should_return_nothing(self):
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, ACTIONS_MAP)
        line = 'this will not be parsed'
        action = unit.action_for(line)
        self.assertIsNone(action)

    def test_basic_full_line_match_returns_message(self):
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, ACTIONS_MAP)
        line = "Marnek enters the realm of the dead"
        expected_message = "Marnek is in skeleton form, shrouded players DPS now"
        self.assertEqual(expected_message, unit.action_for(line).message)

    def test_line_depending_on_character_name_when_character_matches(self):
        unit = MessageGenerator('/path/to/eq', 'tabashir', ACTIONS_MAP)
        line = "shadows will consume you, tabashir"
        expected_message = 'Run away from the raid'
        self.assertEqual(expected_message, unit.action_for(line).message)

    def test_line_depending_on_character_name_when_character_not_matched(self):
        unit = MessageGenerator('/path/to/eq', 'tabashir', ACTIONS_MAP)
        line = "shadows will consume you, anothertoon"
        self.assertIsNone(unit.action_for(line))

    def test_basic_tell(self):
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, ACTIONS_MAP)
        line = "anothertoon tells you, 'hello there'"
        expected_message = 'Incoming Tell'
        self.assertEqual(expected_message, unit.action_for(line).message)

    def test_tell_that_we_ignore(self):
        unit = MessageGenerator('/path/to/eq', 'tabashir', ACTIONS_MAP)
        line = "a vendor tells you, That'll be 10 plat"
        self.assertIsNone(unit.action_for(line))

    def test_mez_returns_background_task(self):
        line = "a mob has been mesmerized"
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, ACTIONS_MAP)
        task = unit.action_for(line)
        self.assertEqual(19, task.timeout)
        self.assertEqual('Mesmerize Warning', task.message)
        self.assertEqual('Mez', task.title)
        expected_command = 'urxvt -iconic -geometry 15x1 -bg red -fg white -title Mez -e python stop_watch.py 19 "Mesmerize Warning" 1'
        self.assertEqual(expected_command, task.command)

if __name__ == '__main__':
    unittest.main()
