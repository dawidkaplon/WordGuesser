from django.db import models
from bs4 import BeautifulSoup
from string import ascii_letters
from queue import Queue

import logging
import random
import requests


logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {levelname:<8} {message}",
    style="{",
    datefmt="%H:%M:%S",
)


class WebScraper:
    """
    The class responsible for scraping data from the Internet.
    Once the data/word is fetched, the Word model inherits from
    this class and takes care of everything else.
    """

    word = models.TextField(default="")
    definition = models.TextField(default="")
    test_flag = False
    result_queue = Queue()
    word_chosen = False

    def fetch_data(self, length, language):
        """
        Fetches an ENGLISH or POLISH data from a given URL by scraping the web.

        Args:
            length (int): The number of letters in target word,

            language (str): The language as string to decide words
            in which language should be fetched

        Returns:
            str: The scraped data (both word and it's definition) from the website.
        """

        while not self.word_chosen:

            if language == "en":
                random_letter = random.choice(list("abcdefghijklmnoprstuw"))
                random_page = random.randint(1, 30)

                url = f"https://www.dictionary.com/list/{random_letter}/{random_page}"
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                try:
                    random_index = random.randint(
                        1, 351
                    )  # Choose random word at selected page (around 350 results per page)
                    self.word = (
                        soup.find("div", class_="sw3o2JSDU4SEB11F3dUQ")
                        .find_all("a")[random_index]
                        .text.upper()
                    )
                    self.definition = soup.find(
                        "div", class_="sw3o2JSDU4SEB11F3dUQ"
                    ).find_all("a")[random_index]["href"]

                except (AttributeError, IndexError):
                    continue

            elif language == "pl":
                random_letter = random.choice(list("abcdefghijklmnoprstuw"))
                random_page = random.randint(0, 300)
                url = f"https://sjp.pwn.pl/lista/{random_letter};{random_page}.html"

                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")

                try:
                    random_index = random.randint(1, 20)
                    self.word = (
                        soup.find("div", class_="col-xs-12 col-sm-4")
                        .find_all("a")[random_index]
                        .text.upper()
                    )
                    self.definition = soup.find(
                        "div", class_="col-xs-12 col-sm-4"
                    ).find_all("a")[random_index]["href"]

                except (AttributeError, IndexError):
                    continue

            if len(self.word) == length and all([letter in ascii_letters for letter in self.word]):
                    self.result_queue.put(self.word)
                    self.result_queue = Queue()
                    self.word_chosen = True
                    logging.info(f"word '{self.word}' has been found")
                    break
            else:
                continue  # Start the word search again if the previous word did not meet the criteria

