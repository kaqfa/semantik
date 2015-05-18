from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Paper(models.Model):
    PAPER_STATUS = (
        ('s', 'Submitted'),
        ('p', 'Pending Review'),
        ('a', 'Accepted'),
    )

    title = models.CharField(max_length=250)
    abstract = models.TextField()
    category = models.ForeignKey(Category)
    keywords = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=PAPER_STATUS, default='s')
    owner = models.ForeignKey(User)


class FileHistory(models.Model):
    for_paper = models.ForeignKey(Paper)
    the_file = models.FileField()
    upload_date = models.DateTimeField(auto_now=True)


class Review(models.Model):
    for_paper = models.ForeignKey(Paper)
    reviewer = models.ForeignKey(User)
    nil_a = models.IntegerField(null=True, blank=True, default=0)
    nil_b = models.IntegerField(null=True, blank=True, default=0)
    nil_c = models.IntegerField(null=True, blank=True, default=0)
    note = models.TextField(blank=True, null=True)