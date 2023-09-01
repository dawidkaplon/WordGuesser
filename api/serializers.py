from rest_framework import serializers
from .scraping.webscraper import WebScraper

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebScraper
        fields = ['result_word', 'result_definition']
