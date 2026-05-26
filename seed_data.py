import os

import django
from django.contrib.auth.hashers import make_password


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turf.settings")
django.setup()

from tapp.models import AccountRole, ApprovalStatus, District, Locations, Login, Package, Turf, User


def account(username, password, role):
    obj, created = Login.objects.get_or_create(
        username=username,
        defaults={"password": make_password(password), "role": role},
    )
    if not created:
        obj.role = role
        if obj.password == password:
            obj.password = make_password(password)
        obj.save(update_fields=["role", "password"])
    return obj


def seed():
    district, _ = District.objects.get_or_create(district="Ernakulam")
    location, _ = Locations.objects.get_or_create(location="Kochi", district=district)

    account("admin", "admin123", AccountRole.ADMIN)

    user_login = account("user", "user123", AccountRole.USER)
    User.objects.get_or_create(
        login=user_login,
        defaults={
            "user_name": "John Doe",
            "user_phone": "9876543210",
            "user_email": "john@example.com",
            "user_contact": "Kochi",
            "district": district,
            "locations": location,
            "status": ApprovalStatus.APPROVED,
        },
    )

    turf_login = account("turf", "turf123", AccountRole.TURF)
    turf, _ = Turf.objects.get_or_create(
        login=turf_login,
        defaults={
            "turf_name": "Soccer City",
            "turf_address": "Kochi Bypass",
            "turf_phone": "9998887776",
            "turf_email": "turf@example.com",
            "turf_ownername": "Turf Owner",
            "turf_squarefeet": "5000",
            "district": district,
            "locations": location,
            "status": ApprovalStatus.APPROVED,
        },
    )

    Package.objects.get_or_create(
        pack_turf=turf,
        pack_name="Morning 5s",
        defaults={
            "pack_rate": 1000,
            "pack_type": "5s",
            "pack_status": ApprovalStatus.APPROVED,
        },
    )

    print("Demo data ready.")
    print("Admin: admin / admin123")
    print("User: user / user123")
    print("Turf owner: turf / turf123")


if __name__ == "__main__":
    seed()
