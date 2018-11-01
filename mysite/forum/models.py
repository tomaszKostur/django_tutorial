from django.db import models

class Autor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    post_date = models.DateTimeField()
    post_text = models.TextField()

    def __str__(self):
        return self.post_text
