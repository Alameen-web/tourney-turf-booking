from django import forms

from .models import (
    ApprovalStatus,
    District,
    Locations,
    Login,
    Package,
    PBooking,
    Turf,
    User,
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class BaseRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    district = forms.ModelChoiceField(queryset=District.objects.all())
    locations = forms.ModelChoiceField(queryset=Locations.objects.select_related("district"))

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if Login.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


class UserRegistrationForm(BaseRegistrationForm):
    user_name = forms.CharField(label="Name", max_length=100)
    user_phone = forms.CharField(label="Phone", max_length=20)
    user_email = forms.EmailField(label="Email", max_length=100)
    user_contact = forms.CharField(label="Address", max_length=100, required=False)

    field_order = [
        "user_name",
        "user_phone",
        "user_email",
        "user_contact",
        "district",
        "locations",
        "username",
        "password",
    ]


class TurfRegistrationForm(BaseRegistrationForm):
    turf_name = forms.CharField(label="Turf name", max_length=100)
    turf_ownername = forms.CharField(label="Owner name", max_length=100, required=False)
    turf_phone = forms.CharField(label="Phone", max_length=20)
    turf_email = forms.EmailField(label="Email", max_length=100)
    turf_address = forms.CharField(label="Address", max_length=300)
    turf_squarefeet = forms.CharField(label="Size", max_length=100, required=False)

    field_order = [
        "turf_name",
        "turf_ownername",
        "turf_phone",
        "turf_email",
        "turf_address",
        "turf_squarefeet",
        "district",
        "locations",
        "username",
        "password",
    ]


class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = [
            "turf_name",
            "turf_ownername",
            "turf_phone",
            "turf_email",
            "turf_address",
            "turf_squarefeet",
            "district",
            "locations",
        ]


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ["pack_name", "pack_rate", "pack_type", "pack_image"]


class BookingForm(forms.ModelForm):
    class Meta:
        model = PBooking
        fields = ["package", "date"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, turf=None, **kwargs):
        self.turf = turf
        super().__init__(*args, **kwargs)
        packages = Package.objects.filter(pack_status=ApprovalStatus.APPROVED)
        if turf:
            packages = packages.filter(pack_turf=turf)
        self.fields["package"].queryset = packages.select_related("pack_turf")

    def clean(self):
        cleaned_data = super().clean()
        package = cleaned_data.get("package")
        booking_date = cleaned_data.get("date")
        if package and booking_date and not PBooking.is_available(package, booking_date):
            raise forms.ValidationError("This package is already booked for that date.")
        return cleaned_data


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ["district"]


class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ["district", "location"]

