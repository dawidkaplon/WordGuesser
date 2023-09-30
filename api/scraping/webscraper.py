from bs4 import BeautifulSoup
from django.db import models

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

    def fetch_data(self, length):
        """
        Fetches data from a given URL by scraping the web.

        Args:
            length (int): The number of letters in target word

        Returns:
            str: The scraped data (both word and it's definition) from the website.
        """

        while True:
            random_letter = random.choice(list("abcdefghijklmnoprstuw"))
            random_page = random.randint(1, 6)

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

                inner_url = soup.find("div", class_="sw3o2JSDU4SEB11F3dUQ").find_all("a")\
                    [random_index]["href"]
                inner_response = requests.get(inner_url)
                inner_soup = BeautifulSoup(inner_response.text, "html.parser")

                self.definition = inner_soup.find(
                    "div", class_="ESah86zaufmd2_YPdZtq"
                ).text.capitalize()

                logging.info("search for a matching word..")

                if WebScraper.test_flag == False:
                    if self.word.isalpha() and len(self.word) == length:
                        logging.info(f"word '{self.word}' has been found")
                        break
                    else:
                        continue  # Start the word search again if the previous word did not meet the criteria

                elif WebScraper.test_flag == True:
                    if self.word.isalpha() and len(self.word) in [3, 4, 5, 6, 7, 8]:
                        logging.info(f"word '{self.word}' has been found")
                        break
                    else:
                        continue

            except (AttributeError, IndexError):
                continue
