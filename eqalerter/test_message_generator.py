#!/usr/bin/env python

import unittest
from message_generator import MessageGenerator

MARNEK1={'expect': 'Marnek enters the realm of the dead', 'message': 'Marnek is in skeleton form, shrouded players DPS now'}
SHADOW6={'expect': 'shadows will consume you, {CHARACTER}', 'message': 'Run away from the raid'}
MEZ={'expect': 'has been mesmerized', 'task': {'title': 'Mez', 'message': 'Mesmerize Warning', 'time': 19}}
GENERALBREAK={'message': 'spell worn off', 'expect': 'spell has worn off'}
TELL={'message': 'Incoming Tell', 'expect': 'tells you,', 'ignore': ["That'll be", "I'll give you", 'Welcome to my bank', 'Come back soon!', "A fine donation! You'll receive", 'We graciously accept your', 'I cannot accept your', 'You have increased your skill in', 'I am unable to wake', 'Attacking']}

IRRELEVANT_CHARACTER = 'nomatter'

class TestMessageGenerator(unittest.TestCase):


    def test_unrecognised_line_should_return_nothing(self):
        action_list = [MARNEK1]
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, action_list)
        line = 'this will not be parsed'
        action = unit.action_for(line)
        self.assertIsNone(action)

    def test_basic_full_line_match_returns_message(self):
        action_list = [MARNEK1]
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, action_list)
        line = "Marnek enters the realm of the dead"
        expected_message = "Marnek is in skeleton form, shrouded players DPS now"
        self.assertEqual(expected_message, unit.action_for(line).message)

    def test_line_depending_on_character_name_when_character_matches(self):
        action_list = [SHADOW6]
        unit = MessageGenerator('/path/to/eq', 'tabashir', action_list)
        line = "shadows will consume you, tabashir"
        expected_message = 'Run away from the raid'
        self.assertEqual(expected_message, unit.action_for(line).message)

    def test_line_depending_on_character_name_when_character_not_matched(self):
        action_list = [SHADOW6]
        unit = MessageGenerator('/path/to/eq', 'tabashir', action_list)
        line = "shadows will consume you, anothertoon"
        self.assertIsNone(unit.action_for(line))

    def test_basic_tell(self):
        action_list = [TELL]
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, action_list)
        line = "anothertoon tells you, 'hello there'"
        expected_message = 'Incoming Tell'
        self.assertEqual(expected_message, unit.action_for(line).message)

    def test_tell_that_we_ignore(self):
        action_list = [TELL]
        unit = MessageGenerator('/path/to/eq', 'tabashir', action_list)
        line = "a vendor tells you, That'll be 10 plat"
        self.assertIsNone(unit.action_for(line))

    def test_mez_returns_background_task(self):
        action_list = [MEZ]
        line = "a mob has been mesmerized"
        unit = MessageGenerator('/path/to/eq', IRRELEVANT_CHARACTER, action_list)
        task = unit.action_for(line)
        self.assertEqual(19, task.timeout)
        self.assertEqual('Mesmerize Warning', task.message)
        self.assertEqual('Mez', task.title)
        expected_command = 'urxvt -iconic -geometry 15x1 -bg red -fg white -title Mez -e python StopWatchTest.py 19 "Mesmerize Warning" 1'
        self.assertEqual(expected_command, task.command)

if __name__ == '__main__':
    unittest.main()
