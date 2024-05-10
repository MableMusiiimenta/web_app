from django.contrib import admin
from .models import Baby, Babyfee, Sitter, SitterPayment, At_school, Shift, Supply, Doll, DollSale


# Register your models here.


admin.site.register(Baby)
admin.site.register(Babyfee)

admin.site.register(Sitter)
admin.site.register(SitterPayment)
admin.site.register(At_school)
admin.site.register(Shift)
admin.site.register(Supply)
admin.site.register(Doll)
admin.site.register(DollSale)

