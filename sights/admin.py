from django.contrib import admin
from .models import AustraliaSight, EurasiaSight, SouthAmericaSight, NorthAmericaSight, AfricaSight, FirstForm
# Register your models here.


admin.site.register(EurasiaSight)
admin.site.register(SouthAmericaSight)
admin.site.register(NorthAmericaSight)
admin.site.register(AfricaSight)
admin.site.register(AustraliaSight)
admin.site.register(FirstForm)