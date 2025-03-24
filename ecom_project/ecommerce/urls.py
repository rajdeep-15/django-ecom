from django.urls import path
from .views import RegisterView,LoginView,ProductListCreateView,ProductDetailView,CartItemListCreateView,CartItemDetailview


urlpatterns = [
    path('register/',RegisterView.as_view(),name = 'register'),
    path('login/', LoginView.as_view(),name = 'login'),
    path('products/',ProductListCreateView.as_view(),name = 'add-products'),
    path('products/<int:id>',ProductDetailView.as_view(),name = 'list-products'),
    path('cart/',CartItemListCreateView.as_view(),name = 'add-cart-items'),
    path('cart/<int:pk>',CartItemDetailview.as_view(),name = 'show-cart')
]


