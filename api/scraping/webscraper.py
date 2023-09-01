from bs4 import BeautifulSoup
from django.db import models
import requests
import random


class WebScraper(models.Model):
    result_word = ''
    result_definition = ''
    
    def fetch_data(self, length):
        """Collect data by passing number as parameter(length of word)"""
        
        while True:
            random_letter = random.choice(list('abcdefghijklmnoprstuw'))
            random_page = random.randint(1, 6)
            
            url = f'https://www.dictionary.com/list/{random_letter}/{random_page}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            
            try:
                random_index = random.randint(1, 351)  # Choose random word at selected page (around 350 results per page)
                
                self.result_word = soup.find('div', class_="sw3o2JSDU4SEB11F3dUQ").find_all('a')[random_index].text.upper()

                inner_url = soup.find('div', class_="sw3o2JSDU4SEB11F3dUQ").find_all('a')[random_index]['href']
                inner_response = requests.get(inner_url)
                inner_soup = BeautifulSoup(inner_response.text, "html.parser")
                
                self.result_definition = inner_soup.find('div', class_='ESah86zaufmd2_YPdZtq').text.capitalize()

                print('search for a matching word..')
                
                if self.result_word.isalpha() and len(self.result_word) == length:
                    print(f"word '{self.result_word}' has been found")
                    break
                else:
                    continue   # Start the word search again if the previous word did not meet the criteria

            except (AttributeError, IndexError):
                continue
