import graphene
from SpiderWeb.helpers import generateID
from .model import AccountModel
from .type import AccountType


class AccountInput(graphene.InputObjectType):
    name = graphene.String()


class AccountCreate(graphene.Mutation):
    class Arguments:
        data = AccountInput(required=True)

    account = graphene.Field(AccountType)

    @staticmethod
    def mutate(root, info, data=None):
        account_instance = AccountModel(
            id=generateID(),
            name=data.name,
            user_id=info.context.user.id,
        )
        account_instance.save()
        return AccountCreate(account=account_instance)


class AccountUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        data = AccountInput(required=True)

    account = graphene.Field(AccountType)

    @staticmethod
    def mutate(root, info, id, data=None):

        instance = AccountModel.objects.get(pk=id)

        if instance:
            if data.name is not None:
                instance.name = data.name
            instance.save()

            return AccountUpdate(account=instance)
        return AccountUpdate(account=None)


class AccountDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        instance = AccountModel.objects.get(pk=id)
        for edge in instance.getEdges():
            edge.delete()
        instance.delete()
        return True


class AccountMutation(graphene.ObjectType):
    create_account = AccountCreate.Field()
    update_account = AccountUpdate.Field()
    delete_account = AccountDelete.Field()
