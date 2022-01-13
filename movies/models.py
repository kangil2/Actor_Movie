from django.db import models





class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    running_time = models.PositiveIntegerField()
    class Meta:
        db_table = 'movies'