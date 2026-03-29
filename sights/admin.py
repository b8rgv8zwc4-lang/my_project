from django.contrib import admin
from .models import (AustraliaSight,
                    EurasiaSight,
                    SouthAmericaSight,
                    NorthAmericaSight,
                    AfricaSight,
                    MoreAboutCountry,
                    Routes, 
                    FoodInCoiuntries,
                    MainCard)
# Register your models here.


admin.site.register(EurasiaSight)
admin.site.register(SouthAmericaSight)
admin.site.register(NorthAmericaSight)
admin.site.register(AfricaSight)
admin.site.register(AustraliaSight)
admin.site.register(MoreAboutCountry)
admin.site.register(Routes)
admin.site.register(FoodInCoiuntries)
admin.site.register(MainCard)
