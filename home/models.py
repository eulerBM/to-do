from django.db import models


class to_do_bank(models.Model):
    key = models.CharField(max_length=250, primary_key=True, unique=True)
    task = models.CharField(max_length=500)
    finished = models.BooleanField()

    def __str__(self):
        return f"Task {self.key}"
