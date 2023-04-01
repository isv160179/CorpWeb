from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from home.models import WebsiteFeatures


@login_required
def index(request):
    context = {'title': 'Мои справки', 'menu_selected': 3,
               'menu': WebsiteFeatures.objects.filter(is_active=True)}
    return render(request, 'reference/index.html', context)
