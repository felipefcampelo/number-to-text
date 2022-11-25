from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .lib import number_to_text


@api_view(['GET', 'POST'])
def num_to_english(request):
    if request.method == 'GET':
        number = request.query_params.get('number')
    elif request.method == 'POST':
        number = request.data['number']
    
    result = number_to_text.convert(number)

    response = {
        "status": result['status'],
        "message": result['data']
    }
    
    return JsonResponse(response)
