import pytest
import datetime
from django.core.exceptions import ValidationError
from rentals.models import Rental, Reservation


@pytest.mark.django_db
class TestRental:

    def test_can_create_rental(self, helpers):
        rental = helpers.create_rental("rental 1")
        assert isinstance(rental, Rental)
        assert rental.__str__() == "rental 1"


@pytest.mark.django_db
class TestReservation:

    def test_can_create_reservation(self, helpers):
        rental = helpers.create_rental("rental 1")
        checkin_date, checkout_date = datetime.date(2022, 1, 3), datetime.date(2022, 1, 16)
        reservation = helpers.create_reservation(rental,
                                                 checkin_date=checkin_date,
                                                 checkout_date=checkout_date)
        assert isinstance(reservation, Reservation)
        assert reservation.__str__() == "RES-1"
        assert reservation.rental_id == rental
        assert reservation.checkin == checkin_date
        assert reservation.checkout == checkout_date

    def test_checkout_must_not_be_earlier_than_checkin(self, helpers):
        rental = helpers.create_rental("rental 1")
        with pytest.raises(ValidationError) as excinfo:
            helpers.create_reservation(rental,
                                       checkin_date=datetime.date(2022, 1, 3),
                                       checkout_date=datetime.date(2022, 1, 2))
        assert "checkout date can't be earlier than checkin date" in str(excinfo)

    def test_cannot_create_reservation_if_rental_is_booked(self, helpers):
        rental = helpers.create_rental("rental 1")
        helpers.create_reservation(rental,
                                   checkin_date=datetime.date(2022, 1, 3),
                                   checkout_date=datetime.date(2022, 1, 24))
        with pytest.raises(ValidationError) as excinfo:
            helpers.create_reservation(rental,
                                       checkin_date=datetime.date(2022, 1, 23),
                                       checkout_date=datetime.date(2022, 2, 1))
        assert "The rental is already booked for this date" in str(excinfo)
