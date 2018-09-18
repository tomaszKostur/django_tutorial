from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Post(models.Model):
    post_date = models.DateTimeField()
    post_text = models.TextField()
#    autor = models.ForeignKey('User', on_delete=models.CASCADE)
    invloved = models.ManyToManyField('User')

    def __str__(self):
        return self.post_text
