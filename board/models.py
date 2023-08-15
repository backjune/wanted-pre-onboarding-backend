from django.db import models
from user.models import User


class Board(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='board', on_delete=models.CASCADE)

    class Meta:
        db_table = "board"
        ordering = ['created']
