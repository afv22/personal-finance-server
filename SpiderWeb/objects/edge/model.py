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

    def _fetchNodeName(self, id):
        return fetch_model(Name.NODE.value).objects.get(pk=id).name

    def __str__(self) -> str:
        return "Fuck"
        # return f"{self._fetchNodeName(self.sourceId)} - {self._fetchNodeName(self.targetId)}"

    def calculateGrossValue(self) -> float:
        sourceAccount = (
            fetch_model(Name.ACCOUNT.value).objects.filter(pk=self.sourceId).first()
        )
        sourceIncome = (
            fetch_model(Name.INCOME.value).objects.filter(pk=self.sourceId).first()
        )

        source = sourceAccount if sourceAccount else sourceIncome

        if self.sourcePercentage:
            return source.calculateGrossValue() * self.sourcePercentage / 100
        elif self.sourceAmount:
            return self.sourceAmount
        return source.calculateRemainingBalance(self)

    def calculateTaxes(self) -> float:
        if not self.isTaxable:
            return 0
        return self.calculateGrossValue() * self.user.calculateRealTaxRate()

    def calculateNetValue(self) -> float:
        return self.calculateGrossValue() - self.calculateTaxes()
