
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    path('', views.HOME, name='home'),
    path('product/<slug:slug>',views.PRODUCT_DETAILS, name='product_detail'),

    # account URL
    path('account/my-account',views.MY_ACCOUNT, name='my_account'),
    path('account/register',views.REGISTER, name='register'),
    path('account/login',views.LOGIN, name='login'),
    path('account/logout',views.logout, name='logout'),
    path('account/profile',views.PROFILE, name='profile'),
    path('checkout',views.CHECKOUT, name='checkout'),
    path('order', views.ORDER, name='orders'),
    path('account/ErrorPage', views.ERROR, name='ErrorPage'),

    # URL for Cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    # Other Page Url
    path('product', views.PRODUCT,name='product'),
    path('product/filter-data',views.filter_data,name="filter-data"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
