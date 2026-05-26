from django.db import models
from django.db.models import Q


class AccountRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    USER = "user", "User"
    TURF = "turf", "Turf owner"


class ApprovalStatus(models.TextChoices):
    WAITING = "waiting", "Waiting"
    APPROVED = "approved", "Approved"
    CANCELLED = "cancelled", "Cancelled"
    REJECTED = "rejected", "Rejected"


class Login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username", max_length=100, unique=True)
    password = models.CharField("password", max_length=128)
    role = models.CharField("role", max_length=10, choices=AccountRole.choices)

    class Meta:
        verbose_name = "login"
        verbose_name_plural = "logins"

    def __str__(self):
        return f"{self.username} ({self.role})"


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district = models.CharField("district", max_length=100, unique=True)

    class Meta:
        ordering = ["district"]
        verbose_name = "district"
        verbose_name_plural = "districts"

    def __str__(self):
        return self.district


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField("location", max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["district__district", "location"]
        verbose_name = "location"
        verbose_name_plural = "locations"
        constraints = [
            models.UniqueConstraint(
                fields=["district", "location"],
                name="unique_location_per_district",
            )
        ]

    def __str__(self):
        if self.district:
            return f"{self.location}, {self.district}"
        return self.location


class Turf(models.Model):
    turf_id = models.AutoField(primary_key=True)
    turf_name = models.CharField("turf_name", max_length=100)
    turf_phone = models.CharField("turf_phone", max_length=20)
    turf_email = models.EmailField("turf_email", max_length=100)
    turf_address = models.CharField("turf_address", max_length=300)
    turf_squarefeet = models.CharField("turf_squarefeet", max_length=100, blank=True)
    turf_ownername = models.CharField("turf_ownername", max_length=100, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True)
    login = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        "status",
        max_length=100,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.WAITING,
    )

    class Meta:
        ordering = ["turf_name"]
        verbose_name = "turf"
        verbose_name_plural = "turfs"

    def __str__(self):
        return self.turf_name

    @property
    def place(self):
        parts = [self.locations, self.district]
        return ", ".join(str(part) for part in parts if part)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField("user_name", max_length=100)
    user_phone = models.CharField("user_phone", max_length=20)
    user_email = models.EmailField("user_email", max_length=100)
    user_contact = models.CharField("user_contact", max_length=100, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True)
    login = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        "status",
        max_length=100,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.APPROVED,
    )

    class Meta:
        ordering = ["user_name"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.user_name


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField("title", max_length=100)
    msg = models.CharField("msg", max_length=300)
    reply = models.CharField("reply", max_length=300, default="pending")

    class Meta:
        ordering = ["-feedback_id"]
        verbose_name = "feedback"
        verbose_name_plural = "feedback"

    def __str__(self):
        return self.title


class Package(models.Model):
    packid = models.AutoField(primary_key=True)
    pack_name = models.CharField("pack_name", max_length=100)
    pack_rate = models.IntegerField()
    pack_type = models.CharField("pack_type", max_length=100)
    pack_image = models.FileField(
        "pack_image",
        max_length=500,
        upload_to="packages/",
        blank=True,
    )
    pack_turf = models.ForeignKey(Turf, on_delete=models.CASCADE, null=True)
    pack_status = models.CharField(
        "pack_status",
        max_length=100,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.APPROVED,
    )

    class Meta:
        ordering = ["pack_turf__turf_name", "pack_name"]
        verbose_name = "package"
        verbose_name_plural = "packages"

    def __str__(self):
        return f"{self.pack_name} - Rs {self.pack_rate}"


class PBooking(models.Model):
    pbookid = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField("date")
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        "status",
        max_length=100,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.WAITING,
    )

    class Meta:
        ordering = ["-date", "-pbookid"]
        verbose_name = "booking"
        verbose_name_plural = "bookings"
        constraints = [
            models.UniqueConstraint(
                fields=["package", "date"],
                condition=Q(status__in=[ApprovalStatus.WAITING, ApprovalStatus.APPROVED]),
                name="unique_active_package_booking_per_date",
            )
        ]

    def __str__(self):
        return f"{self.user} booked {self.package} on {self.date}"

    @classmethod
    def is_available(cls, package, booking_date, exclude_booking=None):
        bookings = cls.objects.filter(
            package=package,
            date=booking_date,
            status__in=[ApprovalStatus.WAITING, ApprovalStatus.APPROVED],
        )
        if exclude_booking:
            bookings = bookings.exclude(pk=exclude_booking.pk)
        return not bookings.exists()


class TurfComplaint(models.Model):
    tcomplaint_id = models.AutoField(primary_key=True)
    tsubject = models.CharField("tsubject", max_length=100)
    tmsg = models.CharField("tmsg", max_length=300)
    tcomplaint_date = models.DateField("tcomplaint_date")
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE, null=True)
    creply = models.CharField("creply", max_length=300, default="pending")

    class Meta:
        ordering = ["-tcomplaint_date"]
        verbose_name = "turf complaint"
        verbose_name_plural = "turf complaints"

    def __str__(self):
        return self.tsubject


# Backwards-compatible aliases for old imports and existing migration names.
login = Login
district = District
locations = Locations
turf = Turf
user = User
feedback = Feedback
package = Package
pbooking = PBooking
turfcomplaint = TurfComplaint
