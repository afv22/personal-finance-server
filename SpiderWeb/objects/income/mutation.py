import graphene
from SpiderWeb.helpers import generateID
from .model import IncomeModel
from .type import IncomeType


class IncomeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    value = graphene.Float(required=True)


class IncomeCreate(graphene.Mutation):
    class Arguments:
        data = IncomeInput(required=True)

    income = graphene.Field(IncomeType)

    @staticmethod
    def mutate(root, info, data=None):
        instance = IncomeModel(
            id=generateID(),
            name=data.name,
            value=data.value,
            user_id=info.context.user.id,
        )
        instance.save()
        return IncomeCreate(income=instance)


class IncomeUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        data = IncomeInput(required=True)

    income = graphene.Field(IncomeType)

    @staticmethod
    def mutate(root, info, id, data=None):

        instance = IncomeModel.objects.get(pk=id)

        if instance:
            instance.name = data.name
            instance.value = data.value
            instance.save()
            return IncomeUpdate(income=instance)
        return IncomeUpdate(income=None)


class IncomeDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        instance = IncomeModel.objects.get(pk=id)
        for edge in instance.getEdges():
            edge.delete()
        instance.delete()
        return True


class IncomeMutation(graphene.ObjectType):
    create_income = IncomeCreate.Field()
    update_income = IncomeUpdate.Field()
    delete_income = IncomeDelete.Field()
