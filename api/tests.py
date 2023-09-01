from django.test import TestCase
import random

from .scraping.webscraper import WebScraper

# Create your tests here.

class WordTest(TestCase):
    
    def test_word_length(self):
        """Verify that length of the word is same as the number given as method's parameter"""
        
        random_length = random.randint(5, 8)
        webscraper = WebScraper()
        webscraper.fetch_data(random_length)
        self.assertEqual(random_length, len(WebScraper.result_word))

    def test_word_spelling(self):
        """Verify that there are no whitespaces, commas, special symbols etc. in the word"""
        
        self.assertTrue(WebScraper.result_word.isalpha())

    
