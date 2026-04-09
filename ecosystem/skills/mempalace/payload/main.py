from django.http import JsonResponse
from mempalace_integration import process_chat, compress_data
def handle_chat(request):
    if request.method == 'POST':
        chat_data = request.POST.dict()
        # Process the chat data using MemPalace's semantic search capabilities
        response = process_chat(chat_data)
        # Compress the response to reduce storage requirements
        compressed_response = compress_data(response)
        return JsonResponse({'response': compressed_response}, safe=False)