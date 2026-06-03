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

def get_regions(request):
    regions = list(
        FarmData.objects.values_list(
            "region",
            flat=True
        ).distinct()
    )

    return JsonResponse(regions, safe=False)

def get_weather(request):
    city = request.GET.get("city")

    data = list(
        FarmData.objects.filter(
            city=city
        ).values(
            "air_temperature_c",
            "relative_humidity",
            "rainfall_mm"
        )[:1]
    )

    return JsonResponse(data, safe=False)

def get_soil(request):
    city = request.GET.get("city")

    data = list(
        FarmData.objects.filter(
            city=city
        ).values(
            "soil_moisture",
            "soil_ph"
        )[:1]
    )

    return JsonResponse(data, safe=False)

def get_health(request):
    city = request.GET.get("city")

    data = list(
        FarmData.objects.filter(
            city=city
        ).values(
            "crop_health_index"
        )[:1]
    )

    return JsonResponse(data, safe=False)

def get_dashboard(request):
    city = request.GET.get("city")

    data = list(
        FarmData.objects.filter(
            city=city
        ).values(
            "state",
            "city",
            "crop_type",
            "air_temperature_c",
            "relative_humidity",
            "rainfall_mm",
            "soil_moisture",
            "soil_ph",
            "crop_health_index",
            "region"
        )[:1]
    )

    return JsonResponse(data, safe=False)