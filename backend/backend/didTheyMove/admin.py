from django.contrib import admin
from .models import DidTheyMove

class DidTheyMoveAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'zipCode', 'phoneNumber', 'client', 'status')

# Register your models here.

admin.site.register(DidTheyMove, DidTheyMoveAdmin)