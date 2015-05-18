from django.contrib.auth.models import User
from django.db import models
from papers.models import Paper


class Fee(models.Model):
    FEE_STATUS = (
        ('w', 'Wait'),
        ('b', 'Billed'),
        ('P', 'Paid'),
    )

    owner = models.ForeignKey(User)
    for_paper = models.ForeignKey(Paper, null=True)
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=FEE_STATUS)


class Payment(models.Model):
    PAYMENT_STATUS = (
        ('p', 'Pending'),
        ('c', 'Confirmed'),
    )

    owner = models.ForeignKey(User)
    amount = models.IntegerField(default=0)
    the_file = models.FileField()
    status = models.CharField(max_length=1, choices=PAYMENT_STATUS)