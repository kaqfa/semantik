from django.contrib import admin
from .models import Payment, Fee


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'amount', 'the_file', 'status']


class FeeAdmin(admin.ModelAdmin):
    list_display = ['owner', 'amount', 'payment_for', 'status']


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Fee, FeeAdmin)