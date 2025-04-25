from django.http import HttpResponse, JsonResponse
from googleapiclient.discovery import build
import os

def googleGraph(request):
    service = build("customsearch", "v1", developerKey=os.environ['GOOGLE_API_KEY'])
    results = service.cse().list(
        q=request.GET['q'], 
        cx=os.environ['CSE_ID'], 
        num=request.GET['num']
    ).execute()
    
    websites = []
    for result in results['items']:
        websites.append({
            'url': result['formattedUrl'],
            'title': result['title'],
            'snippet': result['snippet']
        })
    
    response = {
        'error': False,
        'data': websites
    }

    return JsonResponse(response)