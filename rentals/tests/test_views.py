import datetime

import pytest

from rentals.models import Reservation


@pytest.mark.django_db
def test_all_reservations(client, helpers):
    rental1 = helpers.create_rental("rental 1")
    rental2 = helpers.create_rental("rental 2")
    res1 = helpers.create_reservation(rental1, datetime.date(2022, 1, 5), datetime.date(2022, 1, 13))
    res2 = helpers.create_reservation(rental1, datetime.date(2022, 1, 15), datetime.date(2022, 1, 31))
    res3 = helpers.create_reservation(rental2, datetime.date(2022, 1, 11), datetime.date(2022, 1, 18))
    res4 = helpers.create_reservation(rental2, datetime.date(2022, 1, 21), datetime.date(2022, 1, 21))

    response = client.get("/")
    assert response.status_code == 200
    reservations = response.context["reservations"]
    assert len(reservations) == 4
    assert all(isinstance(r, Reservation) for r in reservations)
    assert reservations[0].previous_reservation_id is None
    assert reservations[1].previous_reservation_id == res1.id
    assert reservations[2].previous_reservation_id is None
    assert reservations[3].previous_reservation_id == res3.id
