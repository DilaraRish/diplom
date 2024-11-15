from django.contrib import admin
from .models import Service, Reviews, Team, Usluga, UslugaPrice, Status, Order, Social


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_name', 'order_phone', 'order_status', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_phone', 'order_status',)



admin.site.register(Service)
admin.site.register(Reviews)
admin.site.register(Team)
admin.site.register(Usluga)
admin.site.register(UslugaPrice)
admin.site.register(Status)
admin.site.register(Order, OrderAdm)
admin.site.register(Social)

