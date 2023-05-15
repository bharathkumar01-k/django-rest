from django.shortcuts import render

from django.http import JsonResponse


def api_response(req,*args,**kwargs):
    return JsonResponse({"message": "Hello My First Django Application"})
