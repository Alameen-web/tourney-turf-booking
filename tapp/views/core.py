from functools import wraps

from django.contrib import messages
from django.contrib.auth.hashers import check_password, identify_hasher, make_password
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_date

from tapp.forms import (
    BookingForm,
    DistrictForm,
    LocationForm,
    LoginForm,
    PackageForm,
    TurfForm,
    TurfRegistrationForm,
    UserRegistrationForm,
)
from tapp.models import (
    AccountRole,
    ApprovalStatus,
    District,
    Feedback,
    Locations,
    Login,
    Package,
    PBooking,
    Turf,
    TurfComplaint,
    User,
)


def _password_matches(raw_password, stored_password):
    try:
        identify_hasher(stored_password)
    except ValueError:
        return raw_password == stored_password
    return check_password(raw_password, stored_password)


def _set_login_session(request, account):
    request.session["id"] = account.logid
    request.session["login_id"] = account.logid
    request.session["username"] = account.username
    request.session["role"] = account.role


def current_account(request):
    login_id = request.session.get("login_id") or request.session.get("id")
    if not login_id:
        return None
    return Login.objects.filter(logid=login_id).first()


def current_customer(request):
    account = current_account(request)
    if not account:
        return None
    return User.objects.filter(login=account).first()


def current_owner_turf(request):
    account = current_account(request)
    if not account:
        return None
    return Turf.objects.filter(login=account).first()


def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.session.get("role") not in allowed_roles:
                messages.error(request, "Please log in to continue.")
                return redirect("login")
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def home(request):
    return render(request, "index.html", {"datast": District.objects.all()})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            account = Login.objects.filter(username=username).first()

            if account and _password_matches(password, account.password):
                if account.password == password:
                    account.password = make_password(password)
                    account.save(update_fields=["password"])

                if account.role == AccountRole.USER:
                    profile = User.objects.filter(login=account).first()
                    if not profile or profile.status != ApprovalStatus.APPROVED:
                        messages.error(request, "Your user account is not approved yet.")
                        return redirect("login")

                if account.role == AccountRole.TURF:
                    turf = Turf.objects.filter(login=account).first()
                    if not turf or turf.status != ApprovalStatus.APPROVED:
                        messages.error(request, "Your turf account is waiting for admin approval.")
                        return redirect("login")

                _set_login_session(request, account)
                messages.success(request, "Logged in successfully.")
                return redirect("dashboard")

            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect("home")


def dashboard(request):
    role = request.session.get("role")
    if role == AccountRole.ADMIN:
        return redirect("adminhome")
    if role == AccountRole.TURF:
        return redirect("turfhome")
    if role == AccountRole.USER:
        return redirect("userhome")
    return redirect("home")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        account = Login.objects.filter(username=username, role=AccountRole.ADMIN).first()
        if account and _password_matches(password, account.password):
            if account.password == password:
                account.password = make_password(password)
                account.save(update_fields=["password"])
            _set_login_session(request, account)
            return redirect("adminhome")
        return render(request, "adminlog.html", {"msg": "invalid username or password"})
    return render(request, "adminlog.html", {"msg": ""})


def user_login_page(request):
    return render(request, "userlog.html")


def old_register_user(request):
    if request.method != "POST":
        return redirect("home")

    try:
        district = District.objects.get(district_id=request.POST.get("district"))
        location = Locations.objects.get(location_id=request.POST.get("location"))
        account = Login.objects.create(
            username=request.POST["username"],
            password=make_password(request.POST["password"]),
            role=AccountRole.USER,
        )
        User.objects.create(
            login=account,
            user_name=request.POST["user_name"],
            user_phone=request.POST["user_phone"],
            user_email=request.POST["user_email"],
            user_contact=request.POST.get("user_contact", ""),
            district=district,
            locations=location,
            status=ApprovalStatus.WAITING,
        )
        messages.success(request, "User registered. Admin approval is required.")
    except (IntegrityError, District.DoesNotExist, Locations.DoesNotExist, KeyError):
        messages.error(request, "Could not register user. Please check the form details.")

    return redirect("home")


def old_register_turf(request):
    if request.method != "POST":
        return redirect("home")

    try:
        district = District.objects.get(district_id=request.POST.get("district"))
        location = Locations.objects.get(location_id=request.POST.get("location"))
        account = Login.objects.create(
            username=request.POST["username"],
            password=make_password(request.POST["password"]),
            role=AccountRole.TURF,
        )
        Turf.objects.create(
            login=account,
            turf_name=request.POST["turf_name"],
            turf_phone=request.POST["turf_phone"],
            turf_email=request.POST["turf_email"],
            turf_address=request.POST["turf_address"],
            turf_squarefeet=request.POST.get("turf_squarefeet", ""),
            turf_ownername=request.POST.get("turf_ownername", ""),
            district=district,
            locations=location,
            status=ApprovalStatus.WAITING,
        )
        messages.success(request, "Turf registered. Admin approval is required.")
    except (IntegrityError, District.DoesNotExist, Locations.DoesNotExist, KeyError):
        messages.error(request, "Could not register turf. Please check the form details.")

    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                account = Login.objects.create(
                    username=form.cleaned_data["username"],
                    password=make_password(form.cleaned_data["password"]),
                    role=AccountRole.USER,
                )
                User.objects.create(
                    login=account,
                    user_name=form.cleaned_data["user_name"],
                    user_phone=form.cleaned_data["user_phone"],
                    user_email=form.cleaned_data["user_email"],
                    user_contact=form.cleaned_data["user_contact"],
                    district=form.cleaned_data["district"],
                    locations=form.cleaned_data["locations"],
                    status=ApprovalStatus.APPROVED,
                )
            except IntegrityError:
                form.add_error("username", "This username is already taken.")
            else:
                messages.success(request, "User account created. You can log in now.")
                return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, "register_user.html", {"form": form})


def register_turf(request):
    if request.method == "POST":
        form = TurfRegistrationForm(request.POST)
        if form.is_valid():
            try:
                account = Login.objects.create(
                    username=form.cleaned_data["username"],
                    password=make_password(form.cleaned_data["password"]),
                    role=AccountRole.TURF,
                )
                Turf.objects.create(
                    login=account,
                    turf_name=form.cleaned_data["turf_name"],
                    turf_ownername=form.cleaned_data["turf_ownername"],
                    turf_phone=form.cleaned_data["turf_phone"],
                    turf_email=form.cleaned_data["turf_email"],
                    turf_address=form.cleaned_data["turf_address"],
                    turf_squarefeet=form.cleaned_data["turf_squarefeet"],
                    district=form.cleaned_data["district"],
                    locations=form.cleaned_data["locations"],
                    status=ApprovalStatus.WAITING,
                )
            except IntegrityError:
                form.add_error("username", "This username is already taken.")
            else:
                messages.success(request, "Turf registered. Admin approval is required before login.")
                return redirect("login")
    else:
        form = TurfRegistrationForm()

    return render(request, "register_turf.html", {"form": form})


def turf_list(request):
    turfs = Turf.objects.filter(status=ApprovalStatus.APPROVED).select_related("district", "locations")
    query = request.GET.get("q", "").strip()
    district_id = request.GET.get("district", "").strip()
    location_id = request.GET.get("location", "").strip()

    if query:
        turfs = turfs.filter(turf_name__icontains=query) | turfs.filter(turf_address__icontains=query)
    if district_id:
        turfs = turfs.filter(district_id=district_id)
    if location_id:
        turfs = turfs.filter(locations_id=location_id)

    context = {
        "turfs": turfs.distinct().order_by("turf_name"),
        "districts": District.objects.all(),
        "locations": Locations.objects.select_related("district"),
        "filters": {"q": query, "district": district_id, "location": location_id},
    }
    return render(request, "turf_list.html", context)


def turf_detail(request, turf_id):
    turf = get_object_or_404(
        Turf.objects.select_related("district", "locations"),
        turf_id=turf_id,
        status=ApprovalStatus.APPROVED,
    )
    packages = Package.objects.filter(pack_turf=turf, pack_status=ApprovalStatus.APPROVED)
    return render(request, "turf_detail.html", {"turf": turf, "packages": packages})


@role_required(AccountRole.USER)
def book_turf(request, turf_id):
    turf = get_object_or_404(Turf, turf_id=turf_id, status=ApprovalStatus.APPROVED)
    customer = current_customer(request)
    if not customer:
        messages.error(request, "User profile not found.")
        return redirect("home")

    if request.method == "POST":
        form = BookingForm(request.POST, turf=turf)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = customer
            booking.turf = turf
            booking.status = ApprovalStatus.WAITING
            booking.save()
            messages.success(request, "Booking request sent to the turf owner.")
            return redirect("booking_history")
    else:
        initial = {}
        package_id = request.GET.get("package")
        if package_id:
            initial["package"] = package_id
        form = BookingForm(turf=turf, initial=initial)

    return render(request, "booking_form.html", {"form": form, "turf": turf})


@role_required(AccountRole.USER)
def booking_history(request):
    customer = current_customer(request)
    bookings = PBooking.objects.none()
    if customer:
        bookings = (
            PBooking.objects.filter(user=customer)
            .select_related("turf", "package")
            .order_by("-date", "-pbookid")
        )
    return render(request, "booking_history.html", {"bookings": bookings})


@role_required(AccountRole.TURF)
def owner_dashboard(request):
    account = current_account(request)
    turf = current_owner_turf(request)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "save_turf":
            form = TurfForm(request.POST, instance=turf)
            if form.is_valid():
                turf = form.save(commit=False)
                turf.login = account
                if not turf.status:
                    turf.status = ApprovalStatus.WAITING
                turf.save()
                messages.success(request, "Turf details saved.")
                return redirect("owner_dashboard")

        if action == "add_package" and turf:
            package_form = PackageForm(request.POST, request.FILES)
            if package_form.is_valid():
                package = package_form.save(commit=False)
                package.pack_turf = turf
                package.pack_status = ApprovalStatus.APPROVED
                package.save()
                messages.success(request, "Package added.")
                return redirect("owner_dashboard")

    turf_form = TurfForm(instance=turf)
    package_form = PackageForm()
    packages = Package.objects.filter(pack_turf=turf) if turf else Package.objects.none()
    bookings = (
        PBooking.objects.filter(turf=turf).select_related("user", "package")
        if turf
        else PBooking.objects.none()
    )

    return render(
        request,
        "owner_dashboard.html",
        {
            "turf": turf,
            "turf_form": turf_form,
            "package_form": package_form,
            "packages": packages,
            "bookings": bookings,
        },
    )


@role_required(AccountRole.TURF)
def owner_booking_action(request, booking_id, action):
    turf = current_owner_turf(request)
    booking = get_object_or_404(PBooking, pbookid=booking_id, turf=turf)

    if request.method == "POST":
        if action == "approve":
            if PBooking.is_available(booking.package, booking.date, exclude_booking=booking):
                booking.status = ApprovalStatus.APPROVED
                booking.save(update_fields=["status"])
                messages.success(request, "Booking approved.")
            else:
                messages.error(request, "That slot is no longer available.")
        elif action == "cancel":
            booking.status = ApprovalStatus.CANCELLED
            booking.save(update_fields=["status"])
            messages.success(request, "Booking cancelled.")

    return redirect("owner_dashboard")


@role_required(AccountRole.ADMIN)
def admin_dashboard(request):
    district_form = DistrictForm()
    location_form = LocationForm()

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "approve_user":
            User.objects.filter(user_id=request.POST.get("user_id")).update(status=ApprovalStatus.APPROVED)
            messages.success(request, "User approved.")

        elif action == "reject_user":
            user = User.objects.filter(user_id=request.POST.get("user_id")).select_related("login").first()
            if user and user.login:
                user.login.delete()
            elif user:
                user.delete()
            messages.success(request, "User rejected.")

        elif action == "approve_turf":
            Turf.objects.filter(turf_id=request.POST.get("turf_id")).update(status=ApprovalStatus.APPROVED)
            messages.success(request, "Turf approved.")

        elif action == "reject_turf":
            turf = Turf.objects.filter(turf_id=request.POST.get("turf_id")).select_related("login").first()
            if turf and turf.login:
                turf.login.delete()
            elif turf:
                turf.delete()
            messages.success(request, "Turf rejected.")

        elif action == "add_district":
            district_form = DistrictForm(request.POST)
            if district_form.is_valid():
                district_form.save()
                messages.success(request, "District added.")
                return redirect("admin_dashboard")

        elif action == "add_location":
            location_form = LocationForm(request.POST)
            if location_form.is_valid():
                location_form.save()
                messages.success(request, "Location added.")
                return redirect("admin_dashboard")

        if action in {"approve_user", "reject_user", "approve_turf", "reject_turf"}:
            return redirect("admin_dashboard")

    context = {
        "pending_users": User.objects.filter(status=ApprovalStatus.WAITING).select_related("district", "locations"),
        "pending_turfs": Turf.objects.filter(status=ApprovalStatus.WAITING).select_related("district", "locations"),
        "approved_users": User.objects.filter(status=ApprovalStatus.APPROVED).count(),
        "approved_turfs": Turf.objects.filter(status=ApprovalStatus.APPROVED).count(),
        "bookings": PBooking.objects.select_related("user", "turf", "package")[:10],
        "district_form": district_form,
        "location_form": location_form,
    }
    return render(request, "admin_dashboard.html", context)


def get_locations(request):
    district_id = request.GET.get("id") or request.GET.get("district")
    locations = Locations.objects.filter(district_id=district_id).order_by("location")
    options = ["<option value=''>Select location</option>"]
    for location in locations:
        options.append(f"<option value='{location.location_id}'>{location.location}</option>")
    return HttpResponse("".join(options))


def legacy_book(request):
    turf_id = request.GET.get("s1") or request.POST.get("s1")
    if not turf_id:
        return redirect("turf_list")
    return book_turf(request, int(turf_id))


def add_complaint(request):
    turf = current_owner_turf(request)
    if request.method == "POST" and turf:
        TurfComplaint.objects.create(
            turf=turf,
            tsubject=request.POST.get("subject", "Complaint"),
            tmsg=request.POST.get("message", ""),
            tcomplaint_date=timezone.localdate(),
        )
        messages.success(request, "Complaint submitted.")
    return redirect("owner_dashboard")


def add_feedback(request):
    customer = current_customer(request)
    if request.method == "POST" and customer:
        Feedback.objects.create(
            user_id=customer,
            title=request.POST.get("title", "Feedback"),
            msg=request.POST.get("message", ""),
        )
        messages.success(request, "Feedback submitted.")
    return redirect(reverse("booking_history"))


@role_required(AccountRole.ADMIN)
def adminhome(request):
    return render(request, "adminhome.html")


@role_required(AccountRole.USER)
def userhome(request):
    return render(request, "userhome.html")


@role_required(AccountRole.TURF)
def turfhome(request):
    return render(request, "turfhome.html")


@role_required(AccountRole.ADMIN)
def add_district(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("district", "").strip()
        if name:
            District.objects.get_or_create(district=name)
            msg = "inserted successfully"
    return render(request, "add_district.html", {"msg": msg})


@role_required(AccountRole.ADMIN)
def list_district(request):
    return render(request, "list_district.html", {"data": District.objects.all()})


@role_required(AccountRole.ADMIN)
def delete_dis(request):
    District.objects.filter(district_id=request.POST.get("s_id")).delete()
    return redirect("list_district")


@role_required(AccountRole.ADMIN)
def add_location(request):
    msg = ""
    if request.method == "POST":
        district = get_object_or_404(District, district_id=request.POST.get("district"))
        location = request.POST.get("location", "").strip()
        if location:
            Locations.objects.get_or_create(district=district, location=location)
            msg = "inserted successfully"
    return render(request, "add_location.html", {"msg": msg, "data": District.objects.all()})


@role_required(AccountRole.ADMIN)
def list_location(request):
    return render(
        request,
        "list_location.html",
        {
            "data": Locations.objects.select_related("district"),
            "dataldt": District.objects.all(),
        },
    )


@role_required(AccountRole.ADMIN)
def edit_location(request):
    location = get_object_or_404(Locations, location_id=request.POST.get("location_id"))
    district_id = request.POST.get("district")
    if district_id:
        location.district = get_object_or_404(District, district_id=district_id)
    location.location = request.POST.get("location", location.location).strip() or location.location
    location.save()
    return redirect("list_location")


@role_required(AccountRole.ADMIN)
def delete_location(request):
    Locations.objects.filter(location_id=request.POST.get("location_id")).delete()
    return redirect("list_location")


@role_required(AccountRole.ADMIN)
def approve_user(request):
    data = User.objects.filter(status=ApprovalStatus.WAITING).select_related("login")
    return render(request, "approve_user.html", {"data": data})


@role_required(AccountRole.ADMIN)
def approved_user(request):
    User.objects.filter(user_id=request.POST.get("user_id")).update(status=ApprovalStatus.APPROVED)
    return redirect("approve_user")


@role_required(AccountRole.ADMIN)
def reject_user(request):
    user = User.objects.filter(user_id=request.POST.get("user_id")).select_related("login").first()
    if user and user.login:
        user.login.delete()
    elif user:
        user.delete()
    return redirect("approve_user")


@role_required(AccountRole.ADMIN)
def list_user(request):
    data = User.objects.filter(status=ApprovalStatus.APPROVED).select_related("login")
    return render(request, "list_user.html", {"data": data})


@role_required(AccountRole.ADMIN)
def delete_user(request):
    user = User.objects.filter(user_id=request.POST.get("user_id")).select_related("login").first()
    if user and user.login:
        user.login.delete()
    elif user:
        user.delete()
    return redirect("list_user")


@role_required(AccountRole.ADMIN)
def approve_turf(request):
    data = Turf.objects.filter(status=ApprovalStatus.WAITING).select_related("login")
    return render(request, "approve_turf.html", {"data": data})


@role_required(AccountRole.ADMIN)
def approved_turf(request):
    Turf.objects.filter(turf_id=request.POST.get("turf_id")).update(status=ApprovalStatus.APPROVED)
    return redirect("approve_turf")


@role_required(AccountRole.ADMIN)
def reject_turf(request):
    turf = Turf.objects.filter(turf_id=request.POST.get("turf_id")).select_related("login").first()
    if turf and turf.login:
        turf.login.delete()
    elif turf:
        turf.delete()
    return redirect("approve_turf")


@role_required(AccountRole.ADMIN)
def list_turf(request):
    data = Turf.objects.filter(status=ApprovalStatus.APPROVED).select_related("login")
    return render(request, "list_turf.html", {"data": data})


@role_required(AccountRole.ADMIN)
def delete_turf(request):
    turf = Turf.objects.filter(turf_id=request.POST.get("turf_id")).select_related("login").first()
    if turf and turf.login:
        turf.login.delete()
    elif turf:
        turf.delete()
    return redirect("list_turf")


@role_required(AccountRole.USER)
def searchturf(request):
    data = Turf.objects.filter(status=ApprovalStatus.APPROVED).select_related("district", "locations")
    return render(request, "allturfs.html", {"data": data})


@role_required(AccountRole.USER)
def book(request):
    turf_id = request.GET.get("s1") or request.POST.get("s1")
    turf = get_object_or_404(Turf, turf_id=turf_id, status=ApprovalStatus.APPROVED)
    packages = Package.objects.filter(pack_turf=turf, pack_status=ApprovalStatus.APPROVED)

    if request.method == "POST":
        customer = current_customer(request)
        package = get_object_or_404(Package, packid=request.POST.get("pack_id"), pack_turf=turf)
        booking_date = parse_date(request.POST.get("booking_date", ""))
        if customer and booking_date and PBooking.is_available(package, booking_date):
            PBooking.objects.create(
                user=customer,
                turf=turf,
                package=package,
                date=booking_date,
                status=ApprovalStatus.WAITING,
            )
            messages.success(request, "Booking request sent.")
            return redirect("usrPackageNewBookings")
        messages.error(request, "This package is already booked for that date.")

    return render(request, "bookturf.html", {"d": turf, "s1": turf.turf_id, "packages": packages})


@role_required(AccountRole.USER)
def user_bookings_by_status(request, status):
    customer = current_customer(request)
    data = PBooking.objects.none()
    if customer:
        data = PBooking.objects.filter(user=customer, status=status).select_related("turf", "package")
    titles = {
        ApprovalStatus.WAITING: "Pending Bookings",
        ApprovalStatus.APPROVED: "Approved Bookings",
        ApprovalStatus.CANCELLED: "Cancelled Bookings",
    }
    return render(request, "usrPackageNewBookings.html", {"data": data, "title": titles.get(status, "Bookings"), "msg": ""})


@role_required(AccountRole.USER)
def usrPackageNewBookings(request):
    return user_bookings_by_status(request, ApprovalStatus.WAITING)


@role_required(AccountRole.USER)
def usrPackageApprovedBookings(request):
    return user_bookings_by_status(request, ApprovalStatus.APPROVED)


@role_required(AccountRole.USER)
def usrPackageCancelledBookings(request):
    return user_bookings_by_status(request, ApprovalStatus.CANCELLED)


@role_required(AccountRole.TURF)
def turfRegisterPackage(request):
    return render(request, "turfRegisterPackage.html", {"msg": ""})


@role_required(AccountRole.TURF)
def turfRegisterPackageProcess(request):
    turf = current_owner_turf(request)
    if turf and request.method == "POST":
        Package.objects.create(
            pack_turf=turf,
            pack_name=request.POST.get("name", ""),
            pack_rate=request.POST.get("rate") or 0,
            pack_type=request.POST.get("type", ""),
            pack_image=request.FILES.get("photo"),
            pack_status=ApprovalStatus.APPROVED,
        )
        messages.success(request, "Package added.")
    return redirect("turfRegisterPackage")


@role_required(AccountRole.TURF)
def turfPackageList(request):
    turf = current_owner_turf(request)
    data = Package.objects.filter(pack_turf=turf) if turf else Package.objects.none()
    return render(request, "turfPackageList.html", {"data": data, "msg": ""})


@role_required(AccountRole.TURF)
def turfPackageUpdate(request):
    turf = current_owner_turf(request)
    package = get_object_or_404(Package, packid=request.POST.get("packid"), pack_turf=turf)
    package.pack_name = request.POST.get("pname", package.pack_name)
    package.pack_rate = request.POST.get("prate") or package.pack_rate
    package.pack_type = request.POST.get("ptype", package.pack_type)
    package.save()
    return redirect("turfPackageList")


@role_required(AccountRole.TURF)
def turfPackageDelete(request):
    turf = current_owner_turf(request)
    Package.objects.filter(packid=request.POST.get("packid"), pack_turf=turf).delete()
    return redirect("turfPackageList")


@role_required(AccountRole.TURF)
def turf_bookings_by_status(request, status, template_name):
    turf = current_owner_turf(request)
    data = PBooking.objects.none()
    if turf:
        data = PBooking.objects.filter(turf=turf, status=status).select_related("user", "package")
    return render(request, template_name, {"data": data, "msg": ""})


@role_required(AccountRole.TURF)
def turfPackageNewBookings(request):
    return turf_bookings_by_status(request, ApprovalStatus.WAITING, "turfPackageNewBookings.html")


@role_required(AccountRole.TURF)
def turfPackageApprovedBookings(request):
    return turf_bookings_by_status(request, ApprovalStatus.APPROVED, "turfPackageApprovedBookings.html")


@role_required(AccountRole.TURF)
def turfPackageCancelledBookings(request):
    return turf_bookings_by_status(request, ApprovalStatus.CANCELLED, "turfPackageCancelledBookings.html")


@role_required(AccountRole.TURF)
def turfPackageBookingApprove(request):
    turf = current_owner_turf(request)
    booking = get_object_or_404(PBooking, pbookid=request.POST.get("pbookid"), turf=turf)
    if PBooking.is_available(booking.package, booking.date, exclude_booking=booking):
        booking.status = ApprovalStatus.APPROVED
        booking.save(update_fields=["status"])
    else:
        messages.error(request, "That package is already booked for the selected date.")
    return redirect("turfPackageNewBookings")


@role_required(AccountRole.TURF)
def turfPackageBookingReject(request):
    turf = current_owner_turf(request)
    PBooking.objects.filter(pbookid=request.POST.get("pbookid"), turf=turf).update(status=ApprovalStatus.CANCELLED)
    return redirect("turfPackageNewBookings")


@role_required(AccountRole.TURF)
def turfPackageRescheduleRequests(request):
    return turf_bookings_by_status(request, "reschedule", "turfPackageRescheduleRequests.html")


@role_required(AccountRole.TURF)
def turfPackageRescheduledBookings(request):
    return turf_bookings_by_status(request, "confirm", "turfPackageRescheduledBookings.html")


@role_required(AccountRole.TURF)
def turfPackageRescheduleApprove(request):
    turf = current_owner_turf(request)
    PBooking.objects.filter(pbookid=request.POST.get("pbookid"), turf=turf).update(status="confirm")
    return redirect("turfPackageRescheduleRequests")


@role_required(AccountRole.TURF)
def turfPackageRescheduleReject(request):
    turf = current_owner_turf(request)
    PBooking.objects.filter(pbookid=request.POST.get("pbookid"), turf=turf).update(status=ApprovalStatus.CANCELLED)
    return redirect("turfPackageRescheduleRequests")


@role_required(AccountRole.TURF)
def turfProfile(request):
    return render(request, "turfProfile.html", {"data": current_owner_turf(request), "msg": ""})


@role_required(AccountRole.TURF)
def turfProfileUpdate(request):
    turf = current_owner_turf(request)
    if turf and request.method == "POST":
        turf.turf_name = request.POST.get("name", turf.turf_name)
        turf.turf_email = request.POST.get("email", turf.turf_email)
        turf.turf_phone = request.POST.get("phone", turf.turf_phone)
        turf.turf_address = request.POST.get("address", turf.turf_address)
        turf.turf_ownername = request.POST.get("owner", turf.turf_ownername)
        turf.turf_squarefeet = request.POST.get("size", turf.turf_squarefeet)
        turf.save()
    return redirect("turfProfile")


def _change_password(request, template_name):
    msg = ""
    if request.method == "POST":
        current = request.POST.get("cpass") or request.POST.get("t1") or ""
        new = request.POST.get("npass") or request.POST.get("t2") or ""
        account = current_account(request)
        if account and _password_matches(current, account.password):
            account.password = make_password(new)
            account.save(update_fields=["password"])
            msg = "Password updated"
        else:
            msg = "invalid current password"
    return render(request, template_name, {"msg": msg})


@role_required(AccountRole.USER)
def userPrivacy(request):
    return _change_password(request, "userPrivacy.html")


@role_required(AccountRole.TURF)
def turfPrivacy(request):
    return _change_password(request, "turfPrivacy.html")


@role_required(AccountRole.ADMIN, AccountRole.USER, AccountRole.TURF)
def privacy(request):
    return _change_password(request, "privacy.html")


@role_required(AccountRole.USER)
def userFeedback(request):
    customer = current_customer(request)
    data = Feedback.objects.filter(user_id=customer) if customer else Feedback.objects.none()
    return render(request, "feedback.html", {"data": data, "msg": ""})


@role_required(AccountRole.USER)
def userAddFeedback(request):
    customer = current_customer(request)
    if customer and request.method == "POST":
        Feedback.objects.create(
            user_id=customer,
            title=request.POST.get("title", ""),
            msg=request.POST.get("msg", ""),
        )
    return redirect("userFeedback")


@role_required(AccountRole.ADMIN)
def user_feedback(request):
    if request.method == "POST":
        Feedback.objects.filter(feedback_id=request.POST.get("t1")).update(reply=request.POST.get("t2", ""))
    return render(request, "user_feed.html", {"data": Feedback.objects.select_related("user_id")})


@role_required(AccountRole.TURF)
def turfComplaints(request):
    turf = current_owner_turf(request)
    data = TurfComplaint.objects.filter(turf=turf) if turf else TurfComplaint.objects.none()
    return render(request, "turfComplaints.html", {"data": data, "msg": ""})


@role_required(AccountRole.TURF)
def turfAddComplaint(request):
    turf = current_owner_turf(request)
    if turf and request.method == "POST":
        TurfComplaint.objects.create(
            turf=turf,
            tsubject=request.POST.get("subject", ""),
            tmsg=request.POST.get("complaint", ""),
            tcomplaint_date=timezone.localdate(),
        )
    return redirect("turfComplaints")


@role_required(AccountRole.ADMIN)
def turf_feed(request):
    if request.method == "POST":
        TurfComplaint.objects.filter(tcomplaint_id=request.POST.get("t1")).update(creply=request.POST.get("t2", ""))
    return render(request, "turf_feed.html", {"data": TurfComplaint.objects.select_related("turf")})


def unavailable_feature(request, *args, **kwargs):
    messages.info(request, "That old menu item was removed during refactoring.")
    return redirect("dashboard")
