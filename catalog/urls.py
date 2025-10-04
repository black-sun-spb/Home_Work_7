from django.urls import path
from . import views
from .views import (
    HomeView, ContactsView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView, products_by_category
)

app_name = "catalog"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('product/<int:pk>/publish/', views.publish_product, name='publish_product'),
    path('product/<int:pk>/unpublish/', views.unpublish_product, name='unpublish_product'),
]
