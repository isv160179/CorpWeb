from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from home.models import WebsiteFeatures



@login_required
def index(request):
    context = {'title': 'Подарки', 'menu_selected': 4,
               'menu': WebsiteFeatures.objects.filter(is_active=True)}
    return render(request, 'gifts/index.html', context)
