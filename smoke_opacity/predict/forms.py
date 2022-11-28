from django import forms


class PreditctForm(forms.Form):
    km = forms.IntegerField(min_value=30000,max_value=400000,label="Distance covered in KM")
    manufacture_date = forms.IntegerField(min_value=2000,max_value=2020,label="Manufacture date")
