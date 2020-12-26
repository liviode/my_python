import unittest2

import cards


class TestStringMethods(unittest2.TestCase):

    def test_code(self):
        c = cards.card_to_code(0)
        self.assertEqual(c, 'SE As')
        c = cards.card_to_code(9)
        self.assertEqual(c, 'SI As')
        c = cards.card_to_code(10)
        self.assertEqual(c, 'SI Kö')

    def test_card_value(self):
        """Card Value Tests"""

        v = cards.card_value(0)
        self.assertEqual(v, 11)

        v = cards.card_value(0, 0)
        self.assertEqual(v, 11)

        v = cards.card_value(9, 0)
        self.assertEqual(v, 11)

        v = cards.card_value(10, 0)
        self.assertEqual(v, 4)

        v = cards.card_value(0, 8)
        self.assertEqual(v, 0)

        # buur
        v = cards.card_value(18 + 3, 18 + 1)
        self.assertEqual(v, 20)

        # buur
        v = cards.card_value(18 + 3, 18)
        self.assertEqual(v, 2)

        # buur (Ro Under, Ro Sechsi)
        print(cards.card_description(18));
        v = cards.card_value(18 + 3, 18+8)
        self.assertEqual(v, 2)



if __name__ == '__main__':
    unittest2.main()
