from django.db import models



class shop(models.Model):
    Name = models.CharField(max_length=150)
    Description = models.TextField()
    Image = models.ImageField(upload_to='picture')
    Price = models.IntegerField()
