from django.contrib import admin
from SpiderWeb.models import EdgeModel, IncomeModel, AccountModel, UserModel, NodeModel

admin.site.register(UserModel)
admin.site.register(EdgeModel)
admin.site.register(AccountModel)
admin.site.register(IncomeModel)
admin.site.register(NodeModel)
