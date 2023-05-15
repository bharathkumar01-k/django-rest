from django.shortcuts import render
import json
from django.http import JsonResponse


def api_response(req,*args,**kwargs):
    return JsonResponse({"message": "Hello My First Django Application"})

def echo_data(request,*args,**kwargs):
    body={}
    query = {}
    print('printing the request',request.GET.dict())
    try:
        query = request.GET.dict() or request.POST.dict()
        body = json.loads(request.body)
    except:
        pass
    if body:
        print('here at if')
        return JsonResponse(body)
    else:
        return JsonResponse(query)
