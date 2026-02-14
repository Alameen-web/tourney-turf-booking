from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('adlogin',views.adlogin,name="adlogin"),
    path('userlog',views.userlog,name="userlog"),
    path('admin',views.admin,name="admin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path("stafflogin",views.stafflogin,name="stafflogin"),
    path("userhome",views.userhome,name="userhome"),
    # path('privacy',views.privacy,name="privacy"),
    path('add_district',views.add_district,name="add_district"),
    path('list_district',views.list_district,name="list_district"),
    path('logout',views.logout,name="logout"),
    path('add_location',views.add_location,name="add_location"),
    path('list_location',views.list_location,name="list_location"),
    path('edit_location',views.edit_location,name="edit_location"),
    path('delete_location',views.delete_location,name="delete_location"),
     path('delete_dis',views.delete_dis,name="delete_dis"),
    path("getLocation/",views.getLocation,name="getLocation"),

    path('userreg',views.userreg,name="userreg"),
    path('turfreg',views.turfreg,name="turfreg"),
    path('approve_user',views.approve_user,name="approve_user"),
    path('approved_user',views.approved_user,name="approved_user"),
    path('reject_user',views.reject_user,name="reject_user"),
    path('list_user',views.list_user,name="list_user"),
    path('delete_user',views.delete_user,name="delete_user"),

    path('userFeedback',views.userFeedback,name="userFeedback"),
    path("userAddFeedback",views.userAddFeedback,name="userAddFeedback"),
    path('user_feedback',views.user_feedback,name="user_feedback"),
    path('turfreg',views.turfreg,name="turfreg"),
    path('approve_turf',views.approve_turf,name="approve_turf"),
    path('approved_turf',views.approved_turf,name="approved_turf"),
    path('reject_turf',views.reject_turf,name="reject_turf"),
    path('list_turf',views.list_turf,name="list_turf"),
    path('delete_turf',views.delete_turf,name="delete_turf"),
    path('turf_feed',views.turf_feed,name="turf_feed"),


    path('usrPackageNewBookings',views.usrPackageNewBookings,name="usrPackageNewBookings"),
    path('usrPackageApprovedBookings',views.usrPackageApprovedBookings,name="usrPackageApprovedBookings"),
    path('usrPackageCancelledBookings',views.usrPackageCancelledBookings,name="usrPackageCancelledBookings"),




    
    path('turfhome',views.turfhome,name="turfhome"),
    path('turfPrivacy',views.turfPrivacy,name="turfPrivacy"),
    path('turfRegisterPackage',views.turfRegisterPackage,name="turfRegisterPackage"),
    path('turfRegisterPackageProcess',views.turfRegisterPackageProcess,name="turfRegisterPackageProcess"),
    path('turfPackageList',views.turfPackageList,name="turfPackageList"),
    path('turfPackageUpdate',views.turfPackageUpdate,name="turfPackageUpdate"),
    path('turfPackageDelete',views.turfPackageDelete,name="turfPackageDelete"),
    path('turfPackageNewBookings',views.turfPackageNewBookings,name="turfPackageNewBookings"),
    path('turfPackageBookingApprove',views.turfPackageBookingApprove,name="turfPackageBookingApprove"),
    path('turfPackageBookingReject',views.turfPackageBookingReject,name="turfPackageBookingReject"),
    path('turfPackageApprovedBookings',views.turfPackageApprovedBookings,name="turfPackageApprovedBookings"),
    path('turfPackageRescheduleRequests',views.turfPackageRescheduleRequests,name="turfPackageRescheduleRequests"),
    path('turfPackageRescheduleApprove',views.turfPackageRescheduleApprove,name="turfPackageRescheduleApprove"),
    path('turfPackageRescheduleReject',views.turfPackageRescheduleReject,name="turfPackageRescheduleReject"),
    path('turfPackageRescheduledBookings',views.turfPackageRescheduledBookings,name="turfPackageRescheduledBookings"),
    path('turfPackageCancelledBookings',views.turfPackageCancelledBookings,name="turfPackageCancelledBookings"),
    path('turfComplaints',views.turfComplaints,name="turfComplaints"),
    path('turfAddComplaint',views.turfAddComplaint,name="turfAddComplaint"),
    path('turfProfile',views.turfProfile,name="turfProfile"),
    path('turfProfileUpdate',views.turfProfileUpdate,name="turfProfileUpdate"),







    path('usershome',views.usershome,name="usershome"),
    path('userPrivacy',views.userPrivacy,name="userPrivacy"),
    path('searchturf',views.searchturf,name='searchturf'),
    path('book',views.book,name="book"),
    path('bookturf',views.bookturf,name="bookturf"),
    path('bookturf',views.bookturf,name="bookturf"),


    # path('app_login',views.app_login,name="app_login"),
    # path('app_register',views.app_register,name="app_register"),
    # path('app_getdistrict',views.app_getdistrict,name="app_getdistrict"),
    # path('app_getlocation',views.app_getlocation,name="app_getlocation"),
    # path('app_getUserProfile',views.app_getUserProfile,name="app_getUserProfile"),
    # path('app_changePassword',views.app_changePassword,name="app_changePassword"),
    # path('app_getTurfList',views.app_getTurfList,name="app_getTurfList"),
    # path('app_getTurfPackages',views.app_getTurfPackages,name="app_getTurfPackages"),
    # path('app_bookPackage',views.app_bookPackage,name="app_bookPackage"),
    # path('app_getPackageBookings',views.app_getPackageBookings,name="app_getPackageBookings"),
    # path('app_rescheduleBooking',views.app_rescheduleBooking,name="app_rescheduleBooking"),
    # path('app_cancelTurfBooking',views.app_cancelTurfBooking,name="app_cancelTurfBooking"),
    # path('app_getRentItems',views.app_getRentItems,name="app_getRentItems"),
    # path('app_bookRentItem',views.app_bookRentItem,name="app_bookRentItem"),
    # path('app_getRentItemBookings',views.app_getRentItemBookings,name="app_getRentItemBookings"),
    # path('app_cancelItemBooking',views.app_cancelItemBooking,name="app_cancelItemBooking"),
    # path('app_getTournament',views.app_getTournament,name="app_getTournament"),
    # path('app_bookTicket',views.app_bookTicket,name="app_bookTicket"),
    # path('app_getBookedTickets',views.app_getBookedTickets,name="app_getBookedTickets"),
    # path('app_getShopList',views.app_getShopList,name="app_getShopList"),
    # path('app_getShopProducts',views.app_getShopProducts,name="app_getShopProducts"),
    # path('app_bookProduct',views.app_bookProduct,name="app_bookProduct"),
    # path('app_getCartItems',views.app_getCartItems,name="app_getCartItems"),
    # path('app_PlaceOrder',views.app_PlaceOrder,name="app_PlaceOrder"),
    # path('app_getOrderHistory',views.app_getOrderHistory,name="app_getOrderHistory"),


    

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)