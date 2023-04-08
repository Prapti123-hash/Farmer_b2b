from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Buyer
from .models import Farmer
from .models import Category
from .models import Payment
from .models import MonetaryHelp
from .models import AddStuble
from .models import ToolsRequired
from .models import ProvideTools
from .models import Wallet
admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(Farmer)
admin.site.register(MonetaryHelp)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(AddStuble)
admin.site.register(ToolsRequired)
admin.site.register(ProvideTools)
admin.site.register(Wallet)