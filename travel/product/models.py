from django.db import models

class TravelPlace(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class comment(models.Model):
    place=models.ForeignKey(TravelPlace,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    cmt=models.TextField()
    date=models.DateTimeField(auto_now_add=True)



    