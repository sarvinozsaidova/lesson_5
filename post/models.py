from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    yaratilgan_sana = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='post/static/images/', blank=True)

    def __str__(self) -> str:
        return self.title
