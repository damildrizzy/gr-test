from django.contrib import admin
from .models import Rental, Reservation


# Register your models here.

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
