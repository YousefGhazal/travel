from django.contrib import admin
from .models import Gallery, City, Hotel, Reservation, ContactUs

# Register your models here.

admin.site.register(Gallery)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(ContactUs)
