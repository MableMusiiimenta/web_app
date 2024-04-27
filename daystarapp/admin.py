from django.contrib import admin
from .models import Baby, Babyfee, Sitter, SitterPayment, At_school, In_school, Supply, Doll, DollSale

class BabyAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "gender"]

# Register your models here.
admin.site.register(Baby, BabyAdmin)
admin.site.register(Babyfee)

class SitterAdmin(admin.ModelAdmin):
    search_fields = ["l_name", "rec_name"]

admin.site.register(Sitter, SitterAdmin)
admin.site.register(SitterPayment)
admin.site.register(At_school)
admin.site.register(In_school)
admin.site.register(Supply)
admin.site.register(Doll)
admin.site.register(DollSale)

