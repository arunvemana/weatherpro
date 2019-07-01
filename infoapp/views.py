from django.shortcuts import render
from infoapp.forms import weather_form
import pyowm

# Create your views here.




def info_view(request):

    apikey = '' # get from the https://openweathermap.org/
    own = pyowm.OWM(apikey)
    a = own.city_id_registry()
    print(a)
    inital_data = {
        'city' :'hyderabad',
        'temp' : 'fahrenheit',
        'logo' : '',
        'get_detailed_status':'cloud'
    }
    form = weather_form(request.POST or None ,initial=inital_data)
    if form.is_valid():
        info = own.weather_at_place(form.cleaned_data['city'])
        if info == '':
            print('aaaaaaaaa')
        w = info.get_weather().get_temperature(unit=form.cleaned_data['TempUnits'][0])
        logo = info.get_weather().get_weather_icon_url()
        status = info.get_weather().get_detailed_status()
        # w = form.cleaned_data['TempUnits']
        print(w)
    else:
        info = own.weather_at_place(inital_data['city'])
        w = info.get_weather().get_temperature(inital_data['temp'])
        logo = info.get_weather().get_weather_icon_url()
        status = info.get_weather().get_detailed_status()

    # a = info.get_weather()
    context = {
        'form':form,
        'w':w,
        'logo':logo,
        'status':status
    }
    # print(w)
    return render(request,'weather.html',{'weatherdetails':context})


def test(request):

    return render(request,'base.html')