from django.db import models
from django.conf import settings
from abc import abstractmethod


class NodeModel(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.user.__str__()}: {self.name}"

    @abstractmethod
    def calculateGrossValue(self):
        pass

    @abstractmethod
    def calculateRemainingBalance(self):
        pass
