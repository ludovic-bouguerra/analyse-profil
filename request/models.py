from django.db import models

class Profile(models.Model):
    url = models.URLField()
    commentaires = models.TextField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{} paye :{}".format(self.url, self.paid)