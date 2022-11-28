from django.shortcuts import render

from .forms import PreditctForm


# Create your views here.
def index(request):
    form = PreditctForm({'km':30000,'manufacture_date':2000})
    context = {'form': form}
    return render(request, 'predict/index.html', context)
