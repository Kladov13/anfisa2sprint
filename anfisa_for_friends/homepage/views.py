from django.shortcuts import render

from django.db.models import Q

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
         'id', 'title', 'price', 'description'
    ).filter(
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True
    ).order_by('title')[1:4]     

    
    context = {
        'ice_cream_list': ice_cream_list,       
    }
    
    return render(request, template, context)
