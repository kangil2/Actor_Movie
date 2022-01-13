import json

from django.views import View
from django.http import JsonResponse

from .models import Actor, ActorMovie


class ActorView(View):
    def get(self, request):
        
        actors = Actor.objects.all()
        
        results = []
        for actor in actors:
            
            actors_movies = ActorMovie.objects.filter(actor_id = actor.id)
            
            movie_list = []
            for actor_movie in actors_movies:
                movie_list.append({
                    "id"    : actor_movie.movie.id,
                    "title" : actor_movie.movie.title,
                    "release_date" : actor_movie.movie.release_date,
                    "running_time" : actor_movie.movie.running_time,
                })

            results.append({
                "first_name" : actor.first_name,
                "last_name"  : actor.last_name,
                "movies" : movie_list
            })
        return JsonResponse({"actors" : results}, status = 200)