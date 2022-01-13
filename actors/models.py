from django.db import models



class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    class Meta:
        db_table = 'actors'
        
        
class ActorMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete = models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete = models.CASCADE)
    class Meta:
        db_table = 'actors_movies'