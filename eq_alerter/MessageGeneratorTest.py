#!/usr/bin/env python

import unittest
from MessageGenerator import *

class TestMessageGenerator(unittest.TestCase):

    def test_unknown_line_should_return_nothing(self):
        line = 'this will not be parsed'
        self.assertIsNone(MessageGenerator.action_for(line, ''))

    def test_basic_full_line_match_returns_message(self):
        line = "Marnek enters the realm of the dead"
        expected_message = "Marnek is in skeleton form, shrouded players DPS now"
        self.assertEqual(expected_message, MessageGenerator.action_for(line, '').message)

    def test_line_depending_on_character_name_when_character_matches(self):
        line = "shadows will consume you, tabashir"
        expected_message = 'Run away from the raid'
        self.assertEqual(expected_message, MessageGenerator.action_for(line, 'tabashir').message)

    def test_line_depending_on_character_name_when_character_not_matched(self):
        line = "shadows will consume you, anothertoon"
        self.assertIsNone(MessageGenerator.action_for(line, 'tabashir'))

    def test_basic_tell(self):
        line = "anothertoon tells you, 'hello there'"
        expected_message = 'Incoming Tell'
        self.assertEqual(expected_message, MessageGenerator.action_for(line, '').message)

    def test_tell_that_we_ignore(self):
        line = "a vendor tells you, That'll be 10 plat"
        self.assertIsNone(MessageGenerator.action_for(line, ''))

    def test_mez_returns_background_task(self):
        line = "a mob has been mesmerized"
        task = MessageGenerator.action_for(line, '')
        self.assertEqual(19, task.timeout)
        self.assertEqual('Mez Warn', task.message)
        self.assertEqual('Mez', task.title)

if __name__ == '__main__':
    unittest.main()
