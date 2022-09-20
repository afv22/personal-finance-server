from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView


def index(request):
    return HttpResponse("Welcome to Eden!")


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass
