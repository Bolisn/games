from django.shortcuts import render

from .models import Gametitle

def game_search_view(request):
    query_dict = request.GET # this is a dictionary
    query = query_dict.get('query') # <input type='text' name='query'/>
 
    try:
        query = int(query_dict.get('query'))
    except:
        query = None
 
    game_obj_obj = None
    if query is not None:
        game_obj = Gametitle.objects.get(id=query)
    context = {
        "object" : game_obj,
    }
    return render(request, "gamename/search.html", context=context)

def game_detail_view(request, id=None):
    game_obj = None
    if id is not None:
        game_obj_obj = Gametitle.objects.get(id=id)
    context = {
        "object":game_obj,
    }
    return render(request, "gamename/detail.html", context=context)
