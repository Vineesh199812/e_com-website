from django.contrib import admin

# Register your models here.
from Owner.models import *

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Carts)
admin.site.register(Orders)
admin.site.register(Reviews)

