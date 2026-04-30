from django.db import models

class User(models.Model):
    name = models.CharField(max_length=244)
    age = models.IntegerField(default=0)


    def str(self):
        return self.name