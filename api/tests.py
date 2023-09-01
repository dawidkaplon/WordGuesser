from django.test import TestCase
import random

from .scraping.webscraper import WebScraper

# Create your tests here.

class WordTest(TestCase):
    global webscraper, random_length

    webscraper = WebScraper()

    random_length = random.randint(5, 8)
    webscraper.fetch_data(random_length)

    def test_word_length(self):
        """Verify that length of the word is same as the number given as method's parameter"""

        self.assertEqual(random_length, len(webscraper.result_word))

    def test_word_spelling(self):
        """Verify that there are no whitespaces, commas, special symbols etc. in the word"""

        self.assertTrue(webscraper.result_word.isalpha())
