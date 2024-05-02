from django.contrib import admin
from .models import Baby, Babyfee, Sitter, SitterPayment, At_school, In_school, Supply, Doll, DollSale


# Register your models here.


admin.site.register(Baby)
admin.site.register(Babyfee)

admin.site.register(Sitter)
admin.site.register(SitterPayment)
admin.site.register(At_school)
admin.site.register(In_school)
admin.site.register(Supply)
admin.site.register(Doll)
admin.site.register(DollSale)

