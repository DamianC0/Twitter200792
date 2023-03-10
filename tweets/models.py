from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    #id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE) #many users can have many tweets
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.content