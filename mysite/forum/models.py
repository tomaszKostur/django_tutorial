from django.db import models

class Autor(models.Model):
    first_name = models.CharField(max_length=20, default='Unknown')
    last_name = models.CharField(max_length=20, default='Unknown')
    nickname = models.CharField(max_length=20, default='Guest')

class Post(models.Model):
    topic = models.CharField(max_length=50, default='General topic')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    post_date = models.DateTimeField()
    post_text = models.TextField()


    def __str__(self):
        return self.post_text
