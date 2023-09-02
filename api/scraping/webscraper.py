import logging
import random

import requests
from bs4 import BeautifulSoup
from django.db import models

logging.basicConfig(level=logging.INFO,
                    format='{asctime} - {levelname:<8} {message}',
                    style='{',
                    datefmt='%H:%M:%S'
                    )


class WebScraper():
    """
    The class responsible for scraping words from the Internet.
    Once the word is fetched, the word model inherits from 
    this class and takes care of everything else.
    """
    
    word = models.TextField(default='')
    definition = models.TextField(default='')
    
    def fetch_data(self, length):
        """Collect data by passing number(length of word) as parameter"""
        
        while True:
            random_letter = random.choice(list('abcdefghijklmnoprstuw'))
            random_page = random.randint(1, 6)
            
            url = f'https://www.dictionary.com/list/{random_letter}/{random_page}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            
            try:
                random_index = random.randint(1, 351)  # Choose random word at selected page (around 350 results per page)
                
                self.word = soup.find('div', class_="sw3o2JSDU4SEB11F3dUQ")\
                    .find_all('a')[random_index].text.upper()

                inner_url = soup.find('div', class_="sw3o2JSDU4SEB11F3dUQ")\
                    .find_all('a')[random_index]['href']
                inner_response = requests.get(inner_url)
                inner_soup = BeautifulSoup(inner_response.text, "html.parser")
                
                self.definition = inner_soup.find('div', class_='ESah86zaufmd2_YPdZtq').text.capitalize()

                logging.info('search for a matching word..')
                
                if self.word.isalpha() and len(self.word) == length:
                    logging.info(f"word '{self.word}' has been found")
                    break
                else:
                    continue   # Start the word search again if the previous word did not meet the criteria

            except (AttributeError, IndexError):
                continue
    
