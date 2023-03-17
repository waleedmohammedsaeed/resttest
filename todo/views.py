from django.shortcuts import render
from django.http import  JsonResponse
from .models import Actions
from .serializer.serializers import ActionsSerializer

# Create your views here.

def todo(request):
    tasks = Actions.objects.all()
    serializer =  ActionsSerializer(tasks, many=True)
    return JsonResponse({'todos': serializer.data})

def action(request, id):
    task = Actions.objects.get(id=id)
    serializer = ActionsSerializer(task, many=False)
    return JsonResponse({'task': serializer.data})
