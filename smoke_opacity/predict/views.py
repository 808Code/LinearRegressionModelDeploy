from django.shortcuts import render

from .forms import PreditctForm


# Create your views here.
def index(request):
    form = PreditctForm()
    context = {'form': form}
    return render(request, 'predict/index.html', context)
