from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



@login_required
def index(request):
    context = {}
    return render(request, 'panel/index.html', context)