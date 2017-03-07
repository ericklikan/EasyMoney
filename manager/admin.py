from django.contrib import admin
from .models import Budget, Transaction, Section
# Register your models here.

admin.site.register(Budget)
admin.site.register(Transaction)
admin.site.register(Section)
