from django.db import models


class Quotes(models.Model):
    simbol = models.CharField(max_length=256, verbose_name="Simbol")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
    time_quote = models.DateTimeField(verbose_name="Time")
    open = models.FloatField(verbose_name="Open")
    high = models.FloatField(verbose_name="High")
    low = models.FloatField(verbose_name="Low")
    close = models.FloatField(verbose_name="Close")
    volume = models.IntegerField(verbose_name="Volume")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.simbol}"

    def delete(self, *args):
        self.deleted = True
        self.save()
