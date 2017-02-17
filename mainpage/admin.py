from django.contrib import admin
from mainpage.models import services_all, staff, home_banner, services_banner, products

# Register your models here.

admin.site.register(services_all)
admin.site.register(staff)
admin.site.register(home_banner)
admin.site.register(services_banner)
admin.site.register(products)


