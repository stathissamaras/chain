from django.urls import path, re_path
from chainapp import views as v
from .views import *


urlpatterns = [
    path('', v.home, name='home'),
    path('filter_dropdown2/', v.filter_dropdown2, name='filter_dropdown2'),
    path("product_detail/<str:pk>/", v.productdetail, name="product_detail"),
    path("contact_us/", v.contactview, name="contact_us"),

    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("mycart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),

    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order/<int:pk>/", CustomerOrderDetailView.as_view(), name="customerorderdetail"),

    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),
    path("search/", SearchView.as_view(), name="search"),

    path("forgot-password/", PasswordForgotView.as_view(), name="passworforgot"),
    path("password-reset/<email>/<token>/",PasswordResetView.as_view(), name="passwordreset"),

    # Admin Side pages

    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(), name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/", AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),

    path("admin-product/list/", AdminProductListView.as_view(), name="adminproductlist"),
]