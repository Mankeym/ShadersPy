from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Shader
# Create your views here.
def main(request):
    shaders = Shader.objects.all()
    return render(request, "main/index.html", { "data": serializers.serialize('json', shaders) })