import graphene
from .model import NodeModel
from .mutation import NodeType


class NodeQuery(graphene.ObjectType):
    pass

    # nodes = graphene.List(NodeType)

    # def resolve_nodes(self, info):
    #     return NodeModel.objects.filter(user_id=info.context.user.id)

    # node = graphene.Field(NodeType, node_id=graphene.ID())

    # def resolve_node(self, info, node_id):
    #     return NodeModel.objects.get(pk=node_id, user_id=info.context.user.id)
