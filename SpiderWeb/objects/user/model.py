from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from .manager import UserManager
from SpiderWeb.helpers import fetch_model, Name
from .utils.taxRate import (
    calculateTieredTaxes,
    MEDICARE_RATE,
    SOCIAL_SECURITY_RATE,
    TAX_BRACKETS,
)
from .utils.states import STATES


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    state = models.CharField(max_length=255, choices=STATES, default="")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"

    def getTaxRate(self) -> float:
        taxableValue = sum(
            map(
                lambda edge: edge.calculateGrossValue(),
                fetch_model(Name.EDGE).objects.filter(isTaxable=True),
            )
        )
        federalTaxes = calculateTieredTaxes(taxableValue, "federal")
        if self.state.lower() in TAX_BRACKETS:
            stateTaxes = (
                calculateTieredTaxes(taxableValue, self.state.lower())
                if self.state.lower()
                else 0
            )
        else:
            stateTaxes = 0
        medicareTaxes = taxableValue * MEDICARE_RATE
        socSecTaxes = taxableValue * SOCIAL_SECURITY_RATE
        totalTaxes = sum([federalTaxes, stateTaxes, medicareTaxes, socSecTaxes])
        return totalTaxes / taxableValue
