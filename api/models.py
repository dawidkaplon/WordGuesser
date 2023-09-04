from django.db import models
from .scraping.webscraper import WebScraper

# Create your models here.


class Word(models.Model, WebScraper):
    """
    This model is supposed to inherit fetched
    word and word's definition from WebScraper class/model.
    It has been created just to keep databases' naming convention
    more clear and obvious.
    """

    word = WebScraper.word
    definition = WebScraper.definition

    def __str__(self) -> str:
        return self.word
