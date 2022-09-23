from SpiderWeb.helpers import fetch_model, Name
from SpiderWeb.objects.node.model import NodeModel


class AccountModel(NodeModel):
    def calculateGrossValue(self) -> float:
        return self.initialValue + sum(
            [edge.calculateNetValue() for edge in self.getIncomingEdges()]
        )

    def calculateNetValue(self) -> float:
        outgoingValue = sum(
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

    def getIncomingEdges(self):
        return fetch_model(Name.EDGE.value).objects.filter(targetId=self.id)

    def getOutgoingEdges(self):
        return fetch_model(Name.EDGE.value).objects.filter(sourceId=self.id)

    def getEdges(self):
        return self.getIncomingEdges() | self.getOutgoingEdges()
