from re import S
import graphene
from .model import UserModel
from .type import UserType
from .utils.states import STATES
from graphql import GraphQLError


class UserCreateInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=False)
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)


class UserCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        data = UserCreateInput(required=True)

    @staticmethod
    def mutate(
        self,
        info,
        data,
    ):
        user = UserModel(
            username=data.username,
            first_name=data.first_name,
        )
        user.set_password(data.password)
        user.save()

        return UserCreate(user=user)


class UserUpdateInput(graphene.InputObjectType):
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)
    state = graphene.String(required=False)


class UserUpdate(graphene.Mutation):
    class Arguments:
        data = UserUpdateInput(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(
        self,
        info,
        data,
    ):
        user = info.context.user
        if user.is_anonymous:
            return False
        instance = UserModel.objects.get(pk=user.id)
        if not instance:
            return False
        if data.first_name is not None:
            instance.first_name = data.first_name
        if data.last_name is not None:
            instance.last_name = data.last_name
        if data.state is not None:
            if data.state not in [state[0] for state in STATES]:
                return GraphQLError("Provided User State not valid")
            instance.state = data.state
        instance.save()
        return True


class UserMutation(graphene.ObjectType):
    create_user = UserCreate.Field()
    update_user = UserUpdate.Field()
