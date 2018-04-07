import unittest
from MessageGenerator import *

class TestMessageGenerator(unittest.TestCase):

    def test_unknown_line_should_return_nothing(self):
        line = 'this will not be parsed'
        self.assertIsNone(MessageGenerator.message_for_line(line, ''))

    def test_basic_full_line_match_returns_message(self):
        line = "Marnek enters the realm of the dead"
        expected_message = "Marnek is in skeleton form, shrouded players DPS now"
        self.assertEqual(expected_message, MessageGenerator.message_for_line(line, ''))

    def test_line_depending_on_character_name_when_character_matches(self):
        line = "shadows will consume you, tabashir"
        expected_message = 'Run away from the raid'
        self.assertEqual(expected_message, MessageGenerator.message_for_line(line, 'tabashir'))

    def test_line_depending_on_character_name_when_character_not_matched(self):
        line = "shadows will consume you, anothertoon"
        self.assertIsNone(MessageGenerator.message_for_line(line, 'tabashir'))

if __name__ == '__main__':
    unittest.main()
