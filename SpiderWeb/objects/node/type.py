import graphene
from graphene_django import DjangoObjectType
from .model import NodeModel


class NodeType(DjangoObjectType):
    class Meta:
        model = NodeModel
        fields = "__all__"

    value = graphene.Float(node_id=graphene.ID())

    def resolve_value(self, info):
        return self.getValue()
