import graphene
from graphene_django import DjangoObjectType
from .model import AccountModel


class AccountType(DjangoObjectType):
    class Meta:
        model = AccountModel
        fields = "__all__"

    gross_value = graphene.Float(required=True)

    def resolve_gross_value(self, info):
        return AccountModel.objects.get(pk=self.id).calculateGrossValue()

    net_value = graphene.Float(required=True)

    def resolve_net_value(self, info):
        return AccountModel.objects.get(pk=self.id).calculateNetValue()
