from django.db import models

class Review(models.Model):
    reviewer = models.CharField(max_length=50)
    message = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=1)

    def __str__(self):
        self.reviewer

class Article(models.Model):
    author_title_date = models.CharField(max_length=500, primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    ip = models.CharField(max_length=20, null=True)
    date = models.DateTimeField()
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.author_title_date
