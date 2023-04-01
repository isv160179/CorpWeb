from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from home.models import WebsiteFeatures


@login_required
def index(request):
    context = {'title': 'Университет', 'menu_selected': 2,
               'menu': WebsiteFeatures.objects.filter(is_active=True)}
    return render(request, 'university/index.html', context)
