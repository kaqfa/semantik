from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Daftar Kategori"

    def __unicode__(self):
        return self.title


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

    class Meta:
        verbose_name = "Makalah"
        verbose_name_plural = "Daftar Makalah"

    def owner_name(self):
        return self.owner.get_full_name()

    def __unicode__(self):
        return self.title


class FileHistory(models.Model):
    for_paper = models.ForeignKey(Paper)
    the_file = models.FileField()
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "File Makalah"
        verbose_name_plural = "File Makalah"


class Review(models.Model):
    for_paper = models.ForeignKey(Paper)
    reviewer = models.ForeignKey(User)
    nil_a = models.IntegerField(null=True, blank=True, default=0)
    nil_b = models.IntegerField(null=True, blank=True, default=0)
    nil_c = models.IntegerField(null=True, blank=True, default=0)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Daftar Review"

    def reviewer_name(self):
        return self.reviewer.get_full_name()

    def paper_title(self):
        return self.for_paper.title