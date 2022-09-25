import graphene
from graphene_django import DjangoObjectType
from .model import IncomeModel


class IncomeType(DjangoObjectType):
    class Meta:
        model = IncomeModel
        fields = "__all__"

    # value = graphene.Float(required=True)

    # def resolve_value(self, info):
    #     return self.payoutValue
