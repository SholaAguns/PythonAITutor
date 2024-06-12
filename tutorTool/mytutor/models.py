from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
from django.utils import timezone


class Query(models.Model):
    user = models.ForeignKey(User, related_name='query', on_delete=models.CASCADE, null=True)
    input = models.TextField(blank=True, default='', max_length=3000)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.published_date = timezone.now()
        # self.save()
        super().save(*args, **kwargs)


class Response(models.Model):
    query = models.ForeignKey(Query, related_name='response', on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True, default='', max_length=3000)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.published_date = timezone.now()
        # self.save()
        super().save(*args, **kwargs)
