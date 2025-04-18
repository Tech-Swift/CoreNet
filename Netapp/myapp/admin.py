from django.contrib import admin

# Register your models here.
from .models import (
    Customers,
    CustomerUsage,
    Discounts,
    Feedback,
    Invoices,
    Payments,
    Plans,
    Subscriptions,
    SupportTickets,
)

admin.site.register(Customers)
admin.site.register(CustomerUsage)
admin.site.register(Discounts)
admin.site.register(Feedback)
admin.site.register(Invoices)
admin.site.register(Payments)
admin.site.register(Plans)
admin.site.register(Subscriptions)
admin.site.register(SupportTickets)
