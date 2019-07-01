from django import forms


class weather_form(forms.Form):
    city = forms.CharField(max_length=100)
    options = (('celsius','celsius'),
               ('fahrenheit','fahrenheit'))
    TempUnits = forms.MultipleChoiceField(choices=options)