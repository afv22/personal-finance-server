from django.contrib import admin
from SpiderWeb.models import EdgeModel, IncomeModel, AccountModel, UserModel

admin.site.register(UserModel)
admin.site.register(EdgeModel)
admin.site.register(AccountModel)
admin.site.register(IncomeModel)
