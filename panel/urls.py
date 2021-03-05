from django.urls import path

from panel import views

urlpatterns = [
    path("", views.panel, name="panel"),
    path("new_product/", views.new_product, name="new_product"),
    path("product/<int:pk>/edit/", views.edit_product, name="edit_product", ),
    path("become_seller/", views.become_seller, name="become_seller"),
    path("products/", views.products, name="products"),
    path("all_products/", views.all_products, name="all_products"),
    path("rate/", views.rate, name="rate"),
]
