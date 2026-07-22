from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "status": "online",
        "message": "Backend de Vlum funcionando."
    })

def custom_404(request, exception):
    return JsonResponse({
        "error": "Not Found",
        "message": "La ruta solicitada no existe"
    }, status=404)
