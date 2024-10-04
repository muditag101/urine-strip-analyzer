from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UrineStripImageForm
import cv2
import numpy as np


def index(request):
    return render(request, "index.html")


@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        form = UrineStripImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            image_path = instance.image.path
            colors = analyze_image(image_path)
            return JsonResponse(colors)
        return JsonResponse({"error": "Invalid form"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def analyze_image(image_path):
    image = cv2.imread(image_path)
    colors = detect_strip_colors(image)
    return colors


def detect_strip_colors(image):
    
    colors = []
    for i in range(10):
        patch = image[i * 10 : (i + 1) * 10, i * 10 : (i + 1) * 10]
        avg_color = cv2.mean(patch)[:3]
        colors.append({"color{}".format(i + 1): avg_color})
    return {"colors": colors}
