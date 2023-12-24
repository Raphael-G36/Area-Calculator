from django.db import models

# Create your models here.
class history (models.Model):
    shape = models.CharField(max_length=100)
    length = models.IntegerField(default=0)
    breadth = models.IntegerField(default=0)
    radius = models.IntegerField(default=0)
    sideLength = models.IntegerField(default=0)
    base = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    pHeight = models.IntegerField(default=0)
    pBase = models.IntegerField(default=0)
    result = models.IntegerField(default=0)

class Meta:
    db_table = 'History'
    
