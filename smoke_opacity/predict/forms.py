from django import forms


class PreditctForm(forms.Form):
    loan_amnt = forms.IntegerField(min_value=0)
    term = forms.IntegerField(min_value=0)
    int_rate = forms.FloatField(min_value=0)