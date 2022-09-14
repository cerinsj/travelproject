from django.db import models

class TravelPlace(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

    