from django.http import JsonResponse
import requests
import settings

def store_knowledge(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        content = request.POST.get('content', '')
        response = requests.post(
            f'{settings.MEMPALACE_BASE_URL}/store/',
            json={'user_id': user_id, 'content': content},
            headers={'Authorization': f'Bearer {settings.MEMPALACE_API_KEY}'}
        )
        return JsonResponse(response.json())