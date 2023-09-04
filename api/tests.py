from django.test import TestCase
from rest_framework.test import APIClient
import random

from api.models import Word
from api.scraping.webscraper import WebScraper

# Create your tests here.


class WordTest(TestCase):
    global webscraper, client, random_id

    client = APIClient()
    random_id = random.randint(1, 5)

    webscraper = Word()
    webscraper.fetch_data(6)

    def setUp(self):
        for w in range(1, 6):
            Word.objects.create(
                word=f"test{str(w)}", definition="This word is being tested."
            )

    def test_word_length(self):
        """
        Verify that length of the word is same 
        as the number given as method's parameter.
        """

        self.assertEqual(6, len(webscraper.word))

    def test_word_spelling(self):
        """
        Verify that there are no whitespaces, commas, 
        special symbols etc. in the word.
        """

        self.assertTrue(webscraper.word.isalpha())

    def test_correct_db_save(self):
        """
        Verify that the word is saved 
        correctly in the database after it is created.
        """

        test_word = Word(word="testing", definition="I am currently under testing.")
        test_word.save()

        self.assertTrue(test_word in Word.objects.all())

    def test_word_id(self):
        """
        Verify that the ID of the specific word correctly 
        matches the data according to the ID provided in the URL.
        """

        test_word = Word.objects.get(id=random_id)
        response = client.get(f"/words/get/{random_id}")
        self.assertEqual(response.json()["word"]["word"], test_word.word)


class URLTest(TestCase):
    global client, WebScraper

    client = APIClient()

    def test_fetch_word(self):
        WebScraper.test_flag = True  # Set a flag to search for words between 3 and 8 letters long instead of just 5.
        response = client.get("/words/get", format="json")
        WebScraper.test_flag = False
        self.assertEqual(response.status_code, 201)

    def test_get_words_list(self):
        response = client.get("/words/list/get", format="json")
        self.assertEqual(response.status_code, 200)

    def test_get_word_details(self):
        response = client.get("/words/get/1")
        self.assertEqual(response.status_code, 200)

    def test_add_word(self):
        response = client.post('/words/add', {'word': 'test', 'definition': 'This word is being tested.'}, format='json')
        self.assertEqual(response.status_code, 201)
