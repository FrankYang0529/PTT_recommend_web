from django.db import models

class Review(models.Model):
    reviewer = models.CharField(max_length=50)
    message = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=1)
    date = models.CharField(max_length=50)

    def __str__(self):
        self.reviewer

class Article(models.Model):
    author_title_date = models.CharField(max_length=500, primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    ip = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(null=True)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.author_title_date

class Recommend_Author(models.Model):
    user = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    score = models.FloatField()

    def __str__(self):
        return self.user

class Relation(models.Model):
    friend = models.CharField(max_length=50)
    relationship = models.IntegerField()

class PTT_User(models.Model):
    user = models.CharField(max_length=50, primary_key=True)
    relations = models.ManyToManyField(Relation)
