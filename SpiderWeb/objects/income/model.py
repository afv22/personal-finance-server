from django.db import models
from SpiderWeb.helpers import fetch_model, Name
from ..node.model import NodeModel


class IncomeModel(NodeModel):
    value = models.FloatField(default=0)

    def getValue(self):
        return self.value

    def getRemainingBalance(self, remaining_edge):
        outgoingValue = sum(
            [
                edge.calculateGrossValue()
                for edge in self.getOutgoingEdges()
                if edge.id != remaining_edge.id
            ]
        )
        return self.getValue() - outgoingValue

    def getOutgoingEdges(self):
        return fetch_model(Name.EDGE).objects.filter(sourceId=self.id)

    def getEdges(self):
        return self.getOutgoingEdges()
