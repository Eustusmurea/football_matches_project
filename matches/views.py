from multiprocessing import context
from django.shortcuts import render
from api_utils import fetch_today_matches

def today_matches_view(request):
    # Call the function to fetch today's matches
    fetch_today_matches()
    
    # Your view logic goes here
    # For example, you can render a template with the fetched data
    
    return render(request, 'matches/today_matches.html', context)
