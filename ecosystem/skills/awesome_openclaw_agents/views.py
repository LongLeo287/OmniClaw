from django.http import JsonResponse
import requests

def fetch_data_view(request):
    url = 'https://api.example.com/data'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)