from django.shortcuts import render
from django.http import JsonResponse
from .models import history
import json


# Create your views here.
def display(request):
    data = list(history.objects.values())
    return JsonResponse(data ,safe=False)


def startCalculator(request):
    if request.method == "POST":
        params = json.loads(request.body)
        shape = params["shape"]
        length =0 if params.get('length') is None else params["length"]  
        breadth =0 if params.get('breadth') is None else params["breadth"]
        radius = 0 if params.get('radius') is None else params["radius"]
        sideLength = 0 if params.get('sideLength') is None else params["sideLength"]
        base = 0 if params.get('base') is None else params["base"]
        height = 0 if params.get('height') is None else params["height"]
        pHeight = 0 if params.get('pHeight') is None else params["pHeight"]
        pBase = 0 if params.get('pBase') is None else params["pBase"]

        if shape == "rectangle":
            result = length * breadth
            response = {"length": length,
                        "breadth": breadth, 
                        "Area": result
                        }
        elif shape =="circle":
             result= 3.142*radius*radius
             response={
                  'shape':shape,
                  'radius':radius,
                  'Area':result
             }
        elif shape=='square':
           result=sideLength*sideLength
           response={
                'shape':shape,
                'sideLength':sideLength,
                'Area': result
           }
        elif shape=='triangle':
           result=0.5*base*height
           response={
                'shape':shape,
                'base':base,
                'height': height,
                'Area':result
           }
        elif shape == 'parallelogram':
           result= pBase*pHeight
           response={
                'shape':shape,
                'pBase':pBase,
                'pHeight':pHeight,
                'Area':result
           }

        db_data= history(
               shape=shape, 
               length=length, 
               breadth=breadth, 
               radius=radius, 
               sideLength=sideLength, 
               base=base, 
               height=height, 
               pHeight=pHeight, 
               pBase=pBase, 
               result=result
           )
        db_data.save()

        return JsonResponse(response)
    else:
          respond={'Error':'please crosscheck the URL you sent'}
          return JsonResponse(respond)
        


