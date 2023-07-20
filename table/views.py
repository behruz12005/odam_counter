from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.shortcuts import render
from .models import Element
from .serializers import ElementSerializer

@api_view(['GET', 'POST'])
def element_list(request):
    if request.method == 'GET':
        elements = Element.objects.all()
        serializer = ElementSerializer(elements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ElementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
def home(request):
    # Oxirgi 10 obyektni olish
    tables = Element.objects.order_by('-id')[:10]

    return render(request, 'home.html', {'tables': tables})
     