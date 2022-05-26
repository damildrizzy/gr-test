# Create your views here.
from django.db.models import Subquery, OuterRef
from django.shortcuts import render

from .models import Reservation


def all_reservations(request):
    reservations = Reservation.objects.select_related().all().order_by("rental_id")
    queryset = reservations.annotate(
        previous_reservation_id=Subquery(
            reservations.filter(rental_id=OuterRef("rental_id"))
                .exclude(checkout__gte=OuterRef("checkout"))
                .order_by("-checkout")
                .values("id")[:1]
        )
    )

    return render(
        request, "reservations.html", {"reservations": queryset}
    )
