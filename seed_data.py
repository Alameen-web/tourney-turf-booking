import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turf.settings')
django.setup()

from tapp.models import *

def seed():
    print("Seeding data...")

    # Create Districts
    d1, created = district.objects.get_or_create(district="Ernakulam")
    d2, created = district.objects.get_or_create(district="Kottayam")
    
    # Create Locations
    l1, created = locations.objects.get_or_create(location="Kochi", district=d1)
    l2, created = locations.objects.get_or_create(location="Pala", district=d2)

    # 1. Admin
    if not login.objects.filter(role="admin").exists():
        admin_login = login.objects.create(username="admin", password="admin123", role="admin")
        print("Admin user created: admin/admin123")
    else:
        print("Admin user already exists.")

    # 2. User
    if not login.objects.filter(username="user").exists():
        user_login = login.objects.create(username="user", password="user123", role="user")
        user.objects.create(
            login=user_login,
            user_name="John Doe",
            user_phone="9876543210",
            user_email="john@example.com",
            user_contact="123 Street",
            district=d1,
            locations=l1,
            status="approved"
        )
        print("User created: user/user123")
    else:
        print("User already exists.")

    # 3. Turf Owner
    if not login.objects.filter(username="turf").exists():
        turf_login = login.objects.create(username="turf", password="turf123", role="turf")
        turf_obj = turf.objects.create(
            login=turf_login,
            turf_name="Soccer City",
            turf_address="Kochi Bypass",
            turf_phone="9998887776",
            turf_email="turf@example.com",
            district=d1,
            locations=l1,
            status="approved",
            turf_ownername="Turf Owner",
            turf_squarefeet="5000"
        )
        print("Turf Owner created: turf/turf123")
    else:
        turf_obj = turf.objects.filter(login__username="turf").first()
        print("Turf Owner already exists.")

    if turf_obj and not package.objects.filter(pack_turf=turf_obj).exists():
        package.objects.create(
            pack_name="Morning 5s",
            pack_rate="1000",
            pack_type="5s",
            pack_turf=turf_obj,
            pack_status="approved",
            pack_image="package/dummy.jpg"
        )
        print("Package created for Turf Owner")

    print("Seeding complete.")

if __name__ == '__main__':
    seed()
