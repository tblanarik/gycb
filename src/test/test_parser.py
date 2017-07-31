import unittest
import gybc.gybc as gybc


class TestGYBCParser(unittest.TestCase):
    def test_found_colors(self):
        sentence = '''COLOR/BEIGE. YEAR/1990. MAKE/HONDA. MODEL/ACCORD. BODY/4-DOOR.
                   LIC/AJA2836. ST/WA. ***DO NOT MAKE CONTACT, CALL 9-1-1***'''
        result = gybc.parse_tweet(sentence)
        self.assertIn('beige', result['color'])

    def test_found_make(self):
        sentence = '''COLOR/BEIGE. YEAR/1990. MAKE/HONDA. MODEL/ACCORD. BODY/4-DOOR.
                   LIC/AJA2836. ST/WA. ***DO NOT MAKE CONTACT, CALL 9-1-1***'''
        result = gybc.parse_tweet(sentence)
        self.assertIn('honda', result['make'])

if __name__ == '__main__':
    unittest.main()
