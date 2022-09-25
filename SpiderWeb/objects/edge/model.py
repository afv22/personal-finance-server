from django.db import models
from django.conf import settings
from SpiderWeb.helpers import fetch_model, Name


class EdgeModel(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sourceId = models.PositiveBigIntegerField()
    targetId = models.PositiveBigIntegerField()
    isTaxable = models.BooleanField(default=False)
    # Only one of these should be set at any given time. Each represents
    # an option for how much of the source balance should be piped through
    sourcePercentage = models.FloatField(default=0)
    sourceAmount = models.FloatField(default=0)
    sourceRemainingBalance = models.BooleanField(default=False)

    def __str__(self) -> str:
        node_obj = fetch_model(Name.NODE).objects
        return f"{self.user.username}: {node_obj.get(pk=self.sourceId).name} - {node_obj.get(pk=self.targetId).name}"

    def calculateGrossValue(self) -> float:
        source = fetch_model(Name.NODE).objects.get(pk=self.sourceId)
        if self.sourcePercentage:
            return source.getValue() * self.sourcePercentage / 100
        elif self.sourceAmount:
            return self.sourceAmount
        return source.getRemainingBalance(self)

    def calculateTaxes(self) -> float:
        return (
            self.calculateGrossValue() * self.user.getTaxRate() if self.isTaxable else 0
        )

    def calculateNetValue(self) -> float:
        return self.calculateGrossValue() - self.calculateTaxes()
