import graphene
from .model import IncomeModel
from .type import IncomeType


class IncomeQuery(graphene.ObjectType):

    incomes = graphene.List(IncomeType)

    def resolve_incomes(self, info, **kwargs):
        return IncomeModel.objects.filter(user_id=info.context.user.id)

    income = graphene.Field(IncomeType, id=graphene.ID())

    def resolve_income(self, info, id):
        IncomeModel.objects.get(pk=id, user_id=info.context.user.id)
