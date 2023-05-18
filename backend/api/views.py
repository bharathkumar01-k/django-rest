from django.shortcuts import render
import json
from django.http import JsonResponse
from products.models import Products


def api_response(req,*args,**kwargs):
    return JsonResponse({"message": "Hello My First Django Application"})

def echo_data(request,*args,**kwargs):
    body={}
    query = request.GET.dict() or request.POST.dict()
    print('printing the request',request.GET.dict())
    try:
        body = json.loads(request.body)
    except:
        pass
    if body:
        print('here at if')
        return JsonResponse(body)
    else:
        return JsonResponse(query)
    
def return_data_from_model(request,*args,**kwargs):
    querySet = Products.objects.values()
    data ={
        "entries":[]
    }

    if querySet:
        for value in querySet:
            print(value)
            entry = {}
            entry["id"] = value["id"]
            entry["Title"] = value["Title"]
            entry["Content"] = value["Content"]
            entry["Price"] = "₹ "+str(value["Price"])
            data["entries"].append(entry)
    return JsonResponse(data)
