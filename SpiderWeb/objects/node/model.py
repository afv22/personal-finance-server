from django.db import models
from django.conf import settings
from SpiderWeb.helpers import fetch_model, Name

subclasses = [Name.ACCOUNT, Name.INCOME]


class NodeModel(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.user.__str__()}: {self.name}"

    def __getChild(self) -> models.Model:
        child = list(
            filter(
                lambda obj: obj,
                map(
                    lambda model: fetch_model(model).objects.filter(pk=self.id).first(),
                    subclasses,
                ),
            )
        )[0]
        return child

    def getRemainingBalance(self, remaining_edge) -> float:
        return self.__getChild().getRemainingBalance(remaining_edge)

    def getValue(self) -> float:
        return self.__getChild().getValue()

    def getEdges(self):
        return self.__getChild().getEdges()
