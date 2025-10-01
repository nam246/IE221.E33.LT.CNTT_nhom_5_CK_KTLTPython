from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def api_login(request):
    """"""
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"status": "ok", 'user': {'username': user.get_username()}}, status=200)
    else:
        return JsonResponse({"status": "error", 'message': 'username or password is incorrect'}, status=400)


@csrf_exempt
def api_logout(request):
    """"""
    logout(request)
    return JsonResponse({"status": "ok", 'message': 'logout successful'}, status=200)
