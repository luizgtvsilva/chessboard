import uuid
from django.db import models

class ChessB(models.Model):

    class Meta:

        db_table = 'chess'
    
    piece_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    initial_position = models.CharField(max_length=200)
    possible_movements = models.CharField(max_length=200)

    def __str__(self):
        return self.piece_name
    
