from django.http import JsonResponse


def ping(request, *args, **kwargs):
    data = {'ping': 'pong!'}
    return JsonResponse(data)
