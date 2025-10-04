from django.db import models
from django.contrib.auth.models import User

class MoviePetition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_petitions')
    created_at = models.DateTimeField(auto_now_add=True)
    voters = models.ManyToManyField(User, related_name='voted_petitions')
    votes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title