from datetime import date

from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from .models import AccountRole, ApprovalStatus, District, Locations, Login, Package, PBooking, Turf, User


class BookingFlowTests(TestCase):
    def setUp(self):
        district = District.objects.create(district="Ernakulam")
        location = Locations.objects.create(district=district, location="Kochi")

        self.user_login = Login.objects.create(
            username="user",
            password=make_password("user123"),
            role=AccountRole.USER,
        )
        self.customer = User.objects.create(
            login=self.user_login,
            user_name="Demo User",
            user_phone="9999999999",
            user_email="user@example.com",
            district=district,
            locations=location,
            status=ApprovalStatus.APPROVED,
        )

        owner_login = Login.objects.create(
            username="turf",
            password=make_password("turf123"),
            role=AccountRole.TURF,
        )
        self.turf = Turf.objects.create(
            login=owner_login,
            turf_name="Soccer City",
            turf_phone="9998887776",
            turf_email="turf@example.com",
            turf_address="Kochi Bypass",
            district=district,
            locations=location,
            status=ApprovalStatus.APPROVED,
        )
        self.package = Package.objects.create(
            pack_turf=self.turf,
            pack_name="Morning 5s",
            pack_rate=1000,
            pack_type="5s",
            pack_status=ApprovalStatus.APPROVED,
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tourney")

    def test_user_can_request_booking(self):
        self.client.post(reverse("login"), {"username": "user", "password": "user123"})
        response = self.client.post(
            reverse("book_turf", args=[self.turf.turf_id]),
            {"package": self.package.packid, "date": "2026-06-01"},
        )
        self.assertRedirects(response, reverse("booking_history"))
        self.assertEqual(PBooking.objects.filter(user=self.customer).count(), 1)

    def test_active_booking_blocks_same_package_and_date(self):
        PBooking.objects.create(
            package=self.package,
            user=self.customer,
            turf=self.turf,
            date=date(2026, 6, 1),
            status=ApprovalStatus.APPROVED,
        )

        self.client.post(reverse("login"), {"username": "user", "password": "user123"})
        response = self.client.post(
            reverse("book_turf", args=[self.turf.turf_id]),
            {"package": self.package.packid, "date": "2026-06-01"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "already booked")
        self.assertEqual(PBooking.objects.count(), 1)
