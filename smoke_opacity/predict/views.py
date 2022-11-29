import pickle

import pandas as pd
from django.shortcuts import render

from .forms import PreditctForm

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
test_data = pd.DataFrame(columns=["KM", "Man. Date"])


# Create your views here.
def index(request):
    context={}
    if request.method == 'GET':
        form = PreditctForm({'km': 38920, 'manufacture_date': 2006})
        context = {'form': form}
    else:
        d = request.POST.dict()
        del d['csrfmiddlewaretoken']
        recieved_values = list(d.values())
        form = PreditctForm(initial=d)
        km = int(recieved_values[0])
        manufacture_date = 2020 - int(recieved_values[1])
        test_data.loc[0] = [km, manufacture_date]
        result = loaded_model.predict(test_data[["KM", "Man. Date"]].to_numpy())[0][0]
        context['form'] = form
        context['prediction'] = round(result, 2)
    return render(request, 'predict/index.html', context)
