import graphene
from .model import AccountModel
from .mutation import AccountType


class AccountQuery(graphene.ObjectType):
    accounts = graphene.List(AccountType)

    def resolve_accounts(self, info):
        return AccountModel.objects.filter(user_id=info.context.user.id)

    account = graphene.Field(AccountType, id=graphene.ID(required=True))

    def resolve_account(self, info, id):
        return AccountModel.objects.get(pk=id, user_id=info.context.user.id)
