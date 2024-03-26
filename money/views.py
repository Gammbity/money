from django.shortcuts import render,redirect
import requests

def google_view(request):
    if request.method == 'POST':
        v = request.POST['search'] 
        if v.lower() == 'valyuta' or v.lower() == 'валюта':
            return redirect ('valyuta')
    return render(request, 'main/google.html')

def home_view(request):
    money = ''
    nbu_buy = '0'
    summa = 0
    response_uz = requests.get(url='https://nbu.uz/uz/exchange-rates/json/').json()
    response_en = requests.get(url="https://nbu.uz/en/exchange-rates/json/").json()
    if request.method == 'GET':
        if 'money' in request.GET:
            money = request.GET['money'][:3]
            nbu_buy = request.GET['money'][4::]
    if request.method == 'GET':
        if 'summa' in request.GET:
            if request.GET['summa'] == '':
                return redirect('valyuta')
            summa = request.GET['summa']
            nbu_buy = f"{float(nbu_buy) * int(summa)}"              
    return render(request, 'main/valyuta.html', context={
        'response_en':response_en,
        'nbu_buy':nbu_buy,
        'summa':summa,
        'response_uz':response_uz,
        'money':money
    })  