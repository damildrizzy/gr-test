import pytest
from rentals.models import Rental, Reservation


class Helpers:
    @staticmethod
    def create_rental(name):
        return Rental.objects.create(name=name)

    @staticmethod
    def create_reservation(rental, checkin_date, checkout_date):
        return Reservation.objects.create(rental_id=rental, checkin=checkin_date, checkout=checkout_date)


@pytest.fixture()
def helpers():
    return Helpers
