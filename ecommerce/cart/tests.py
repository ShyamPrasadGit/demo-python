from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('removie/int(product_id>/',views.cart.cart_remove,name='cart_remove)'),
    path('full_removie/int(product_id>/', views.full__remove, name='full_remove)')

]