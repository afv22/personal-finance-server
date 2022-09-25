import graphene
import graphql_jwt
from graphql_auth import mutations

from SpiderWeb.objects.edge.query import EdgeQuery
from SpiderWeb.objects.income.query import IncomeQuery
from SpiderWeb.objects.account.query import AccountQuery
from SpiderWeb.objects.user.query import UserQuery
from SpiderWeb.objects.node.query import NodeQuery

from SpiderWeb.objects.edge.mutation import EdgeMutation
from SpiderWeb.objects.income.mutation import IncomeMutation
from SpiderWeb.objects.account.mutation import AccountMutation
from SpiderWeb.objects.user.mutation import UserMutation
from SpiderWeb.objects.node.mutation import NodeMutation


class Query(
    AccountQuery, EdgeQuery, IncomeQuery, NodeQuery, UserQuery, graphene.ObjectType
):
    pass


class Mutation(
    AccountMutation,
    EdgeMutation,
    IncomeMutation,
    NodeMutation,
    UserMutation,
    graphene.ObjectType,
):
    register = mutations.Register.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
