from django.http import JsonResponse
from .models import FarmData

def get_states(request):
    states = list(
        FarmData.objects.values_list("state", flat=True).distinct()
    )
    return JsonResponse(states, safe=False)

