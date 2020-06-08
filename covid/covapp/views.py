from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    if request.method == 'POST':
        x = str(request.POST.get('country'))
        querystring = {"country":x}
    else:
        querystring = {"country":"India"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "b246a253cfmshf2132c2b2da08c4p151375jsna52d1b4d4bec"
        }

    response = requests.request("GET", url, headers=headers,params=querystring).json()
    data = response["response"]
    try:
        d = data[0]
    except IndexError:
        return render(request,'covapp/index.html')

    print(d)
    context ={
    'all':d['cases']['total'],
    'recovered':d['cases']['recovered'],
    'active':d['cases']['active'],
    'deaths':d['deaths']['total'],
    'ndeaths':d['deaths']['new'],
    'ncases':d['cases']['new'],
    'critical':d['cases']['critical'],
    'country':querystring['country'],
    'continent':d['continent'],
    'day':d['day'],
    'time':d['time'],
    'population':d['population'],
    'ttest':d['tests']['total'],
        }
    return render(request,'covapp/index.html',context)
