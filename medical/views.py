import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import result
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@login_required(login_url="/login/")
def index(request):
    if request.method == "GET":
        all_result = result.objects.all().order_by("-created_at")
        main = all_result.first()
        rest_results = all_result.exclude(pk=main.id)[:10]
        return render(request, "medical/index.html",{"main": main,"results": rest_results})

@login_required(login_url="/login/")
def all_results(request):
    if request.method == "GET":
        all_result = result.objects.all().order_by("-created_at")
        return render(request, "medical/all_result.html",{"results": all_result})

@login_required(login_url="/login/")
def result_info(request, result_id):
    if request.method == "GET":
        main = get_object_or_404(result, pk=result_id)
        return render(request, "medical/result.html",{"main": main})

def login_view(request):
    if request.method == "GET":
        return render(request, "medical/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "medical/login.html",{"wrong": True})



def logout_view(request):
    if request.method == "GET":
        logout(request)
        return render(request, "medical/login.html",{"out": True})

@csrf_exempt
def arduino_data(request):
    if request.method == 'POST':
        # Parse JSON data from request body
        try:
            arduino_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Extract data fields
        temp = arduino_data.get('temp')
        press = arduino_data.get('press')
        h_rate = arduino_data.get('h_rate')
        b_oxy = arduino_data.get('b_oxy')
        sugar = arduino_data.get('sugar')

        # Save the data to the database
        try:
            result_object = result.objects.create(
                temp=temp,
                press=press,
                h_rate=h_rate,
                b_oxy=b_oxy,
                Sugar=sugar
            )
            return JsonResponse({'message': 'Data received and saved successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)