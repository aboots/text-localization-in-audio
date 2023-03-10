import json
import time

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import UserQueryRequestForm
from .models import UserQueryRequest

from .engine import usage


def ping(request):
    return HttpResponse("pong")


def ping_template(request):
    return render(request, "ping_en.html", {"time": time.time()})


def search(request):
    return render(request, "search_en.html")


@csrf_exempt
def search_submit(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    if not request.FILES:
        return HttpResponseBadRequest("No file")
    form = UserQueryRequestForm(request.POST, request.FILES)
    if not form.is_valid():
        return HttpResponseBadRequest("Invalid form")
    form.save()
    return render(request, "waiting_en.html", {"id": form.instance.id})


@csrf_exempt
def process(request, id):
    query_request = UserQueryRequest.objects.get(id=id)
    wave_file_path = query_request.audio_wave_file.path
    query_text = query_request.query_text
    usage.usage(wave_file_path, query_text, 0)
    return HttpResponse("Done")


@csrf_exempt
def results(request, id):
    query_request = UserQueryRequest.objects.get(id=id)
    wave_file_path = query_request.audio_wave_file.path

    with open(wave_file_path + ".json") as f:
        data = json.load(f)
    result = list(data.values())[0]

    context = {
        'audio_url': query_request.audio_wave_file.url,
        'results': result
    }

    return render(request, "results_en.html", context)
