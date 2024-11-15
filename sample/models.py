from django.db import models


class SampleSettings(models.Model):
    tg_token = models.CharField(max_length=200)
    tg_chat = models.CharField(max_length=200)
    tg_message = models.TextField()

    def __str__(self):
        return self.tg_chat
