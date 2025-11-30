from django.test import TestCase

class BasicTest(TestCase):
    def test_math(self):
        self.assertEqual(2 + 2, 4)
