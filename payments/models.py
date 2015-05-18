from django.contrib.auth.models import User
from django.db import models
from papers.models import Paper


class Fee(models.Model):
    FEE_STATUS = (
        ('w', 'Wait'),
        ('b', 'Billed'),
        ('P', 'Paid'),
    )

    FEE_FOR = (
        ('s', 'Seminar'),
        ('p', 'Pemakalah'),
        ('t', 'Makalah Tambahan'),
    )

    owner = models.ForeignKey(User)
    for_paper = models.ForeignKey(Paper, null=True, blank=True)
    payment_for = models.CharField(max_length=1, choices=FEE_FOR, default='p')
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=FEE_STATUS)

    class Meta:
        verbose_name = "Biaya"
        verbose_name_plural = "Daftar Biaya"

    def owner_name(self):
        return self.owner.get_full_name()


class Payment(models.Model):
    PAYMENT_STATUS = (
        ('p', 'Pending'),
        ('c', 'Confirmed'),
    )

    owner = models.ForeignKey(User)
    amount = models.IntegerField(default=0)
    the_file = models.FileField()
    status = models.CharField(max_length=1, choices=PAYMENT_STATUS)

    class Meta:
        verbose_name = "Pembayaran"
        verbose_name_plural = "Daftar Pembayaran"

    def owner_name(self):
        return self.owner.get_full_name()