from django.contrib import admin
from .models import Baby, Babyfee
from .models import Sitter, SitterPayment
# Register your models here.
admin.site.register(Baby)
admin.site.register(Sitter)
admin.site.register(Babyfee)
admin.site.register(SitterPayment)
