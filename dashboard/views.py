from django.http import JsonResponse
from .models import FarmData

def get_states(request):
    states = list(
        FarmData.objects.values_list("state", flat=True).distinct()
    )
    return JsonResponse(states, safe=False)

def get_cities(request):
    state = request.GET.get("state")

    cities = list(
        FarmData.objects.filter(
            state=state
        ).values_list(
            "city",
            flat=True
        ).distinct()
    )

    return JsonResponse(cities, safe=False)

def get_crops(request):
    state = request.GET.get("state")

    crops = list(
        FarmData.objects.filter(
            state=state
        ).values_list(
            "crop_type",
            flat=True
        ).distinct()
    )

    return JsonResponse(crops, safe=False)