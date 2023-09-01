from django.shortcuts import render
from django.http import JsonResponse
from .serializers import WordSerializer
from .scraping.webscraper import WebScraper

# Create your views here.

def get_word(request):
    webscraper = WebScraper()
    webscraper.fetch_data(6)
    
    if webscraper.result_word is not None:
        serializer = WordSerializer(webscraper)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Failure'}, safe=False)