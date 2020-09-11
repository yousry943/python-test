from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from bson import ObjectId
from bson.json_util import loads, dumps

from pymongo import MongoClient

def coffee_machines(request,product_type,data):
    client = MongoClient('mongodb://localhost:27017')
    db = client.testapp
    querys = db.ahmedtest
    for query in querys.find({product_type:data}):

        print(query)




    return JsonResponse(query)

    #return  print(bills_post)

    #return JnsoResponse(bills_post)
# Create your views here.
