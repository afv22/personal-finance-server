import graphene
from .type import EdgeType
from .model import EdgeModel


class EdgeQuery(graphene.ObjectType):

    edges = graphene.List(EdgeType)

    def resolve_edges(self, info):
        return EdgeModel.objects.filter(user_id=info.context.user.id)

    edge = graphene.Field(EdgeType, edge_id=graphene.ID())

    def resolve_edge(self, info, edge_id):
        return EdgeModel.objects.get(pk=edge_id, user_id=info.context.user.id)

    edges_from_source_id = graphene.List(EdgeType, source_id=graphene.ID())

    def resolve_edges_from_source_id(self, info, source_id):
        return EdgeModel.objects.filter(
            sourceId=source_id, user_id=info.context.user.id
        )

    edges_from_target_id = graphene.List(EdgeType, target_id=graphene.ID())

    def resolve_edges_from_target_id(self, info, target_id):
        return EdgeModel.objects.filter(
            targetId=target_id, user_id=info.context.user.id
        )
