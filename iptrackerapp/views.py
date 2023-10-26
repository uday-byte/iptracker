from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from iptrackerapp.models import IPAddress
from django.utils import timezone
import requests

@csrf_exempt
def track_ip(request):
    if request.method == 'GET':
        public_ip = requests.get('https://api.ipify.org?format=json').json().get('ip')
        ip_address = IPAddress(ip_address=public_ip)
        ip_address.save()
        return JsonResponse({'message': 'IP address recorded successfully!'})
    else:
        return JsonResponse({'message': 'Invalid request method!'}, status=400)



