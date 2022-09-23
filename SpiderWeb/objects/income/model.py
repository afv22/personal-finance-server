from django.db import models
from SpiderWeb.helpers import fetch_model, Name
from ..node.model import NodeModel


class IncomeModel(NodeModel):
    value = models.FloatField(default=1.0)

    def calculateGrossValue(self) -> float:
        return self.value

    def calculateNetValue(self) -> float:
        outgoingValue = self.value + sum(
            [edge.calculateGrossValue() for edge in self.getOutgoingEdges()]
        )
        return self.calculateGrossValue() - outgoingValue

    def calculateRemainingBalance(self, remaining_edge):
        outgoingValue = sum(
            [
                edge.calculateGrossValue()
                for edge in self.getOutgoingEdges()
                if edge.id != remaining_edge.id
            ]
        )
        return self.calculateGrossValue() - outgoingValue

    def getOutgoingEdges(self):
        return fetch_model(Name.EDGE.value).objects.filter(sourceId=self.id)

    def getEdges(self):
        return self.getOutgoingEdges()
