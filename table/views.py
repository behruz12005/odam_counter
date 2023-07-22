from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Element
from datetime import date
from .serializers import ElementSerializer
import pandas as pd
import sqlite3
import json


df = pd.DataFrame()
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
    # <-- ------------------------------ ->
    #Datani pandasga utqazib olish 

    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table_element")

    results = cursor.fetchall()
    databese = pd.DataFrame(results, columns=["id", "name", "data", "values", "voqt"])

    cursor.close()
    connection.close()

    # <-- ------------------------------ ->
    #Bugun kun data olish 

    def today(x):
        today = date.today()
        d1 = today.strftime("%d")
        m1 = today.strftime("%m")
        y1 = today.strftime("%Y")
        if x[0:4] == y1 and x[5:7] == m1 and x[8:10] == d1:
            return True
        else:
            return False
    df = pd.DataFrame()
    today_data = databese[databese['data'].apply(today)]
    df['munit'] = today_data['voqt'].apply(lambda x: x[0:2])
    df['values'] = today_data['values']


    #Malumotlarni dict qilib js berilish uchun tahlash 

    dict = [
        {'time': 0, 'value': 0},
        {'time': 1, 'value': 0},
        {'time': 2, 'value': 0},
        {'time': 3, 'value': 0},
        {'time': 4, 'value': 0},
        {'time': 5, 'value': 0},
        {'time': 6, 'value': 0},
        {'time': 7, 'value': 0},
        {'time': 8, 'value': 0},
        {'time': 9, 'value': 0},
        {'time': 10, 'value': 0},
        {'time': 11, 'value': 0},
        {'time': 12, 'value': 0},
        {'time': 13, 'value': 0},
        {'time': 14, 'value': 0},
        {'time': 15, 'value': 0},
        {'time': 16, 'value': 0},
        {'time': 17, 'value': 0},
        {'time': 18, 'value': 0},
        {'time': 19, 'value': 0},
        {'time': 20, 'value': 0},
        {'time': 21, 'value': 0},
        {'time': 22, 'value': 0},
        {'time': 23, 'value': 0},
        {'time': 24, 'value': 0},

    ]
    dict2 = [
        {'time': 0, 'value': 0},
        {'time': 1, 'value': 0},
        {'time': 2, 'value': 0},
        {'time': 3, 'value': 0},
        {'time': 4, 'value': 0},
        {'time': 5, 'value': 0},
        {'time': 6, 'value': 0},
        {'time': 7, 'value': 0},
        {'time': 8, 'value': 0},
        {'time': 9, 'value': 0},
        {'time': 10, 'value': 0},
        {'time': 11, 'value': 0},
        {'time': 12, 'value': 0},
        {'time': 13, 'value': 0},
        {'time': 14, 'value': 0},
        {'time': 15, 'value': 0},
        {'time': 16, 'value': 0},
        {'time': 17, 'value': 0},
        {'time': 18, 'value': 0},
        {'time': 19, 'value': 0},
        {'time': 20, 'value': 0},
        {'time': 21, 'value': 0},
        {'time': 22, 'value': 0},
        {'time': 23, 'value': 0},
        {'time': 24, 'value': 0},

    ]

    # Oxirgi 10 obyektni olish
    
    tables = Element.objects.order_by('-id')[:10]
    df['munit'] = df['munit'].apply(lambda x: x[0:2])
    up = df[df['values'] == 'up'].groupby(['munit']).count()
    down = df[df['values'] == 'dow'].groupby(['munit']).count()


    for i in range(len(dict)):
        for m, v in up['values'].items():
            if int(dict[i]['time']) == int(m):
                dict[i]['value'] = v

    for i in range(len(dict2)):
        for m, v in down['values'].items():
            if int(dict2[i]['time']) == int(m):
                dict2[i]['value'] = v
    dict_up = json.dumps(dict)
    dict_down = json.dumps(dict2)
    

    return render(request, 'home.html', {'tables': tables,'dict_up':dict_up,'dict_down':dict_down})
