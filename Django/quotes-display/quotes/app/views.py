import requests
from django.shortcuts import render

def quotes(request):
    response = requests.get('https://dummyjson.com/quotes/random')
    quote_data = response.json()

    context = {
        'quote': quote_data['quote'],
        'author': quote_data['author']
    }
    return render(request, 'index.html', context)
