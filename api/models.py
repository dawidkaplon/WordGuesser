from django.db import models
from .scraping.webscraper import WebScraper

# Create your models here.

class Word(models.Model, WebScraper):
    """Create another class/model to make the naming convention simpler"""

    word = WebScraper.word
    definition = WebScraper.definition
    
    def __str__(self) -> str:
        return self.word
    