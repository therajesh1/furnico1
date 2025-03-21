# ecommerce/urls.py

from django.urls import path
from eco import views
from .views import register_shopkeeper, register_customer
from .views import SofaView, MandirView, TableView, ChairView, CupboardView, ShoeView

from django.urls import path


from django.urls import path




urlpatterns = [
    path('', views.home, name='home'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('product-search/', views.product_search, name='product-search'),
    path('internship_registration/', views.internship_registration, name='internship_registration'),

    # path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
     # Ensure this is defined
    path('register_shopkeeper/', views.register_shopkeeper, name='register_shopkeeper'),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('signin/', views.signin, name='signin'),
    path('add_product/', views.add_product, name='add_product'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # URL for logout
    path('manage-products/', views.manage_products, name='manage_products'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('toggle-stock-status/<int:product_id>/', views.toggle_stock_status, name='toggle_stock_status'),
    path('sofa/', SofaView.as_view(), name='sofa'),
    path('mandir/', MandirView.as_view(), name='mandir'),
    path('table/', TableView.as_view(), name='table'),
    path('chair/', ChairView.as_view(), name='chair'),
    path('cupboard/', CupboardView.as_view(), name='cupboard'),
    path('shoerack/', ShoeView.as_view(), name='shoerack'),

    # urls.py
    path("<str:shop_name>-<str:city>/", views.shop_products, name="shop_products"),

        # Product Detail and Buy Now
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),  # URL for logout

    # Order Summary and Payment Processing
    # path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),

    path('process_payment/<int:order_id>/', views.process_payment, name='process_payment'),

    # Customer Orders and Shopkeeper Orders
    path('customer_orders/', views.customer_orders, name='customer_orders'),
    path('shopkeeper_orders/', views.shopkeeper_orders, name='shopkeeper_orders'),
   


]

# urls.py

