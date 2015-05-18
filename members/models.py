from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    USER_ROLE = (
        ('a', 'Admin'),
        ('p', 'Pemakalah'),
        ('s', 'Seminar'),
        ('r', 'Reviewer'),
    )

    USER_STATUS = (
        ('a', 'Aktif'),
        ('b', 'Banned'),
    )

    owner = models.OneToOneField(User)
    institution = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=1, choices=USER_ROLE, default='p')
    status = models.CharField(max_length=1, choices=USER_STATUS, default='a')

    class Meta:
        verbose_name = "Profil Pengguna"
        verbose_name_plural = "Daftar Pengguna"

    def owner_name(self):
        return self.owner.get_full_name()


class Message(models.Model):
    MESSAGE_STATUS = (
        ('s', 'Terkirim'),
        ('r', 'Terbaca'),
        ('d', 'Terhapus'),
    )

    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=MESSAGE_STATUS, default='s')

    class Meta:
        verbose_name = "Pesan"
        verbose_name_plural = "Daftar Pesan"

    def sender_name(self):
        return self.sender.get_full_name()

    def receiver_name(self):
        return self.receiver.get_full_name()