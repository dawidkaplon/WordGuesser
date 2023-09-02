from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import WordSerializer
from .models import Word

# Create your views here.

@api_view(['GET',])
def get_single_word(request):
    
    if request.method == 'GET':
        webscraper = Word()
        webscraper.fetch_data(5)
        
        if webscraper.word is not None:
            serializer = WordSerializer(webscraper)
            word = Word(word=webscraper.word, definition = webscraper.definition)
            word.save() # Create a found word and save it in the database
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Failure'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['GET',])
def get_all_words(request):

    if request.method == 'GET':
        all_words = Word.objects.all()
        serializer = WordSerializer(all_words, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    

@api_view(['POST',])
def add_word(request):
    
    if request.method == 'POST':
        serializer = WordSerializer(data=request.data)

        # Save the data
        word = request.data['word']
        definition = request.data['definition']
        
        if serializer.is_valid():
            # Create and save a new Word object with the extracted data
            word = Word(word=word, definition=definition)
            word.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def word_details(request, id):
    
    if request.method == 'GET':
        try:
            word = Word.objects.get(id=id)
        except Word.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = WordSerializer(word)
        return JsonResponse(serializer.data, safe=False)
