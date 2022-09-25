from urllib import request
import graphene
from graphene_django import DjangoObjectType
from .model import AccountModel


class AccountType(DjangoObjectType):
    class Meta:
        model = AccountModel
        fields = "__all__"

    value = graphene.Float(required=True)

    def resolve_value(self, info):
        return self.getValue()

    net_value = graphene.Float(required=True)

    def resolve_net_value(self, info):
        return self.getNetValue()
