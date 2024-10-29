from django.db import models


# Create your models here.
class GEResults(models.Model):
    constituency = models.CharField(max_length=255)
    conservative = models.IntegerField()
    labour = models.IntegerField()
    liberaldemocrat = models.IntegerField()
    reform = models.IntegerField()
    majority = models.IntegerField()
    combined_conreform = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.constituency}"
