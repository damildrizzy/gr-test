from django.db import models
from django.core.exceptions import ValidationError


class Rental(models.Model):
    name = models.CharField(max_length=214)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"RES-{self.id}"

    def _validate_checkout_date(self):
        if self.checkin > self.checkout:
            raise ValidationError(
                {"checkout": "checkout date can't be earlier than checkin date"}
            )

    def _validate_rental_availability(self):
        previous_reservation = Reservation.objects.filter(rental_id=self.rental_id).last()
        if previous_reservation and previous_reservation.checkout > self.checkin:
            raise ValidationError(
                {"checkin": "The rental is already booked for this date"}
            )

    def clean(self):
        self._validate_checkout_date()
        self._validate_rental_availability()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
