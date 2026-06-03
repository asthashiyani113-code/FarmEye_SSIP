from django.http import JsonResponse
from .models import FarmData

def get_states(request):
    states = list(
        FarmData.objects.values_list("state", flat=True).distinct().order_by("state")
    )
    return JsonResponse(states, safe=False)

def get_cities(request):
    state = request.GET.get("state")
    cities = list(
        FarmData.objects.filter(state=state)
        .values_list("city", flat=True).distinct().order_by("city")
    )
    return JsonResponse(cities, safe=False)

def get_crops(request):
    state = request.GET.get("state")
    city = request.GET.get("city", None)
    qs = FarmData.objects.filter(state=state)
    if city:
        qs = qs.filter(city=city)
    crops = list(qs.values_list("crop_type", flat=True).distinct().order_by("crop_type"))
    return JsonResponse(crops, safe=False)

def get_regions(request):
    regions = list(
        FarmData.objects.values_list("region", flat=True).distinct().order_by("region")
    )
    return JsonResponse(regions, safe=False)

def get_weather(request):
    city = request.GET.get("city")
    data = list(
        FarmData.objects.filter(city=city).values(
            "air_temperature_c",
            "relative_humidity",
            "rainfall_mm",
            "wind_speed_mps",
            "solar_radiation_wm2",
        )[:1]
    )
    return JsonResponse(data, safe=False)

def get_soil(request):
    city = request.GET.get("city")
    crop = request.GET.get("crop", None)
    qs = FarmData.objects.filter(city=city)
    if crop:
        qs = qs.filter(crop_type=crop)
    data = list(
        qs.values(
            "soil_moisture",
            "soil_ph",
            "soil_temperature_c",
            "irrigation_status",
            "fertilizer_applied",
        )[:1]
    )
    return JsonResponse(data, safe=False)

def get_health(request):
    city = request.GET.get("city")
    crop = request.GET.get("crop", None)
    qs = FarmData.objects.filter(city=city)
    if crop:
        qs = qs.filter(crop_type=crop)
    data = list(
        qs.values(
            "crop_health_index",
            "pest_risk_level",
            "growth_stage",
            "crop_duration_days",
        )[:1]
    )
    return JsonResponse(data, safe=False)

def get_dashboard(request):
    city = request.GET.get("city")
    crop = request.GET.get("crop", None)
    qs = FarmData.objects.filter(city=city)
    if crop:
        qs = qs.filter(crop_type=crop)
    data = list(
        qs.values(
            "state", "city", "crop_type", "region",
            "air_temperature_c", "relative_humidity", "rainfall_mm",
            "wind_speed_mps", "solar_radiation_wm2",
            "soil_moisture", "soil_ph", "soil_temperature_c",
            "crop_health_index", "pest_risk_level",
            "growth_stage", "crop_duration_days",
            "irrigation_status", "fertilizer_applied",
        )[:1]
    )
    return JsonResponse(data, safe=False)
