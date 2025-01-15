from django.http import HttpResponse
from django.template.loader import render_to_string
from gamename.models import Gametitle
import random
 
def home_view(request):
   
    rand_int = random.randint(1, 3) #rand_id = 1, 2 or 3
    game = Gametitle.objects.get(id= rand_int)
    game_queryset = Gametitle.objects.all()
 
    context = {
        "game_list": game_queryset,
        "id" : game.id,
        "title" : game.title,
        "content" : game.content
    }
 
    HTML_STRING = render_to_string("home-view.html", context=context)
 
    return HttpResponse(HTML_STRING)