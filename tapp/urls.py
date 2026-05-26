from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),

    # Login and registration routes used by the restored frontend.
    path("admin", views.admin_login, name="admin"),
    path("adlogin", views.admin_login, name="adlogin"),
    path("userlog", views.user_login_page, name="userlog"),
    path("stafflogin", views.login_view, name="stafflogin"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("logout", views.logout_view, name="logout_old"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("userreg", views.old_register_user, name="userreg"),
    path("turfreg", views.old_register_turf, name="turfreg"),
    path("register/user/", views.register_user, name="register_user"),
    path("register/turf/", views.register_turf, name="register_turf"),

    # Old dashboard pages.
    path("adminhome", views.adminhome, name="adminhome"),
    path("userhome", views.userhome, name="userhome"),
    path("turfhome", views.turfhome, name="turfhome"),

    # Admin district/location management.
    path("add_district", views.add_district, name="add_district"),
    path("list_district", views.list_district, name="list_district"),
    path("delete_dis", views.delete_dis, name="delete_dis"),
    path("add_location", views.add_location, name="add_location"),
    path("list_location", views.list_location, name="list_location"),
    path("edit_location", views.edit_location, name="edit_location"),
    path("delete_location", views.delete_location, name="delete_location"),
    path("getLocation/", views.get_locations, name="getLocation"),
    path("get-locations/", views.get_locations, name="get_locations"),

    # Admin approval/list pages.
    path("approve_user", views.approve_user, name="approve_user"),
    path("approved_user", views.approved_user, name="approved_user"),
    path("reject_user", views.reject_user, name="reject_user"),
    path("list_user", views.list_user, name="list_user"),
    path("delete_user", views.delete_user, name="delete_user"),
    path("approve_turf", views.approve_turf, name="approve_turf"),
    path("approved_turf", views.approved_turf, name="approved_turf"),
    path("reject_turf", views.reject_turf, name="reject_turf"),
    path("list_turf", views.list_turf, name="list_turf"),
    path("delete_turf", views.delete_turf, name="delete_turf"),

    # User turf browsing and bookings.
    path("searchturf", views.searchturf, name="searchturf"),
    path("book", views.book, name="book"),
    path("bookturf", views.book, name="bookturf"),
    path("usrPackageNewBookings", views.usrPackageNewBookings, name="usrPackageNewBookings"),
    path("usrPackageApprovedBookings", views.usrPackageApprovedBookings, name="usrPackageApprovedBookings"),
    path("usrPackageCancelledBookings", views.usrPackageCancelledBookings, name="usrPackageCancelledBookings"),

    # Turf owner package and booking pages.
    path("turfRegisterPackage", views.turfRegisterPackage, name="turfRegisterPackage"),
    path("turfRegisterPackageProcess", views.turfRegisterPackageProcess, name="turfRegisterPackageProcess"),
    path("turfPackageList", views.turfPackageList, name="turfPackageList"),
    path("turfPackageUpdate", views.turfPackageUpdate, name="turfPackageUpdate"),
    path("turfPackageDelete", views.turfPackageDelete, name="turfPackageDelete"),
    path("turfPackageNewBookings", views.turfPackageNewBookings, name="turfPackageNewBookings"),
    path("turfPackageBookingApprove", views.turfPackageBookingApprove, name="turfPackageBookingApprove"),
    path("turfPackageBookingReject", views.turfPackageBookingReject, name="turfPackageBookingReject"),
    path("turfPackageApprovedBookings", views.turfPackageApprovedBookings, name="turfPackageApprovedBookings"),
    path("turfPackageCancelledBookings", views.turfPackageCancelledBookings, name="turfPackageCancelledBookings"),
    path("turfPackageRescheduleRequests", views.turfPackageRescheduleRequests, name="turfPackageRescheduleRequests"),
    path("turfPackageRescheduleApprove", views.turfPackageRescheduleApprove, name="turfPackageRescheduleApprove"),
    path("turfPackageRescheduleReject", views.turfPackageRescheduleReject, name="turfPackageRescheduleReject"),
    path("turfPackageRescheduledBookings", views.turfPackageRescheduledBookings, name="turfPackageRescheduledBookings"),
    path("turfProfile", views.turfProfile, name="turfProfile"),
    path("turfProfileUpdate", views.turfProfileUpdate, name="turfProfileUpdate"),
    path("turfPrivacy", views.turfPrivacy, name="turfPrivacy"),
    path("turfComplaints", views.turfComplaints, name="turfComplaints"),
    path("turfAddComplaint", views.turfAddComplaint, name="turfAddComplaint"),

    # Feedback/privacy pages.
    path("privacy", views.privacy, name="privacy"),
    path("userPrivacy", views.userPrivacy, name="userPrivacy"),
    path("userFeedback", views.userFeedback, name="userFeedback"),
    path("userAddFeedback", views.userAddFeedback, name="userAddFeedback"),
    path("user_feedback", views.user_feedback, name="user_feedback"),
    path("turf_feed", views.turf_feed, name="turf_feed"),

    # Clean routes retained for easier explanation and future use.
    path("turfs/", views.turf_list, name="turf_list"),
    path("turfs/<int:turf_id>/", views.turf_detail, name="turf_detail"),
    path("turfs/<int:turf_id>/book/", views.book_turf, name="book_turf"),
    path("bookings/", views.booking_history, name="booking_history"),
    path("owner/", views.owner_dashboard, name="owner_dashboard"),
    path("owner/bookings/<int:booking_id>/<str:action>/", views.owner_booking_action, name="owner_booking_action"),
    path("owner/complaints/add/", views.add_complaint, name="add_complaint"),
    path("feedback/add/", views.add_feedback, name="add_feedback"),
    path("site-admin/", views.admin_dashboard, name="admin_dashboard"),

    # Removed legacy modules: keep URL names so old sidebars do not crash.
    path("shopreg", views.unavailable_feature, name="shopreg"),
    path("clubreg", views.unavailable_feature, name="clubreg"),
    path("approve_shop", views.unavailable_feature, name="approve_shop"),
    path("list_shop", views.unavailable_feature, name="list_shop"),
    path("shop_feed", views.unavailable_feature, name="shop_feed"),
    path("approve_club", views.unavailable_feature, name="approve_club"),
    path("list_club", views.unavailable_feature, name="list_club"),
    path("club_feed", views.unavailable_feature, name="club_feed"),
    path("tour_approve", views.unavailable_feature, name="tour_approve"),
    path("turfAddItems", views.unavailable_feature, name="turfAddItems"),
    path("turfRentItems", views.unavailable_feature, name="turfRentItems"),
    path("turfRentItemNewBookings", views.unavailable_feature, name="turfRentItemNewBookings"),
    path("turfRentItemApprovedBookings", views.unavailable_feature, name="turfRentItemApprovedBookings"),
    path("turfRentItemRejectedBookings", views.unavailable_feature, name="turfRentItemRejectedBookings"),
    path("turfRentItemCancelledBookings", views.unavailable_feature, name="turfRentItemCancelledBookings"),
]
