from SpiderWeb.helpers import fetch_model, Name
from SpiderWeb.objects.node.model import NodeModel


class AccountModel(NodeModel):
    def getValue(self):
        return sum([edge.calculateNetValue() for edge in self.getIncomingEdges()])

    def getNetValue(self):
        return self.getValue() - sum(
            [edge.calculateGrossValue() for edge in self.getOutgoingEdges()]
        )

    def getRemainingBalance(self, remaining_edge):
        outgoingValue = sum(
            [
                edge.calculateGrossValue()
                for edge in self.getOutgoingEdges()
                if edge.id != remaining_edge.id
            ]
        )
        return self.getValue() - outgoingValue

    def getIncomingEdges(self):
        return fetch_model(Name.EDGE).objects.filter(targetId=self.id)

    def getOutgoingEdges(self):
        return fetch_model(Name.EDGE).objects.filter(sourceId=self.id)

    def getEdges(self):
        return self.getIncomingEdges() | self.getOutgoingEdges()
