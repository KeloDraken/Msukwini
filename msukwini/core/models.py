from django.db import models


class Feedback(models.Model):
    email = models.CharField(max_length=1000, null=False, blank=False)
    name = models.CharField(max_length=1000, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.email
