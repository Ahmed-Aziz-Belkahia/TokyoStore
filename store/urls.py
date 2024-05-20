from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("compare/", views.compare, name="compare"),
    path("my-account/", views.my_account, name="my_account"),
    path("product-categories-4-column-sidebar/", views.product_categories_4_column_sidebar, name="product_categories_4_column_sidebar"),
    path("product-categories-5-column-sidebar/", views.product_categories_5_column_sidebar, name="product_categories_5_column_sidebar"),
    path("product-categories-6-column-full-width/", views.product_categories_6_column_full_width, name="product_categories_6_column_full_width"),
    path("product-categories-7-column-full-width/", views.product_categories_7_column_full_width, name="product_categories_7_column_full_width"),
    path("shop-3-columns-sidebar/", views.shop_3_columns_sidebar, name="shop_3_columns_sidebar"),
    path("shop-4-columns-sidebar/", views.shop_4_columns_sidebar, name="shop_4_columns_sidebar"),
    path("shop-5-columns-sidebar/", views.shop_5_columns_sidebar, name="shop_5_columns_sidebar"),
    path("shop-6-columns-full-width/", views.shop_6_columns_full_width, name="shop_6_columns_full_width"),
    path("shop-7-columns-full-width/", views.shop_7_columns_full_width, name="shop_7_columns_full_width"),
    path("shop-full-width/", views.shop_full_width, name="shop_full_width"),
    path("shop-grid-extended/", views.shop_grid_extended, name="shop_grid_extended"),
    path("shop-grid/", views.shop_grid, name="shop_grid"),
    path("shop-left-sidebar/", views.shop_left_sidebar, name="shop_left_sidebar"),
    path("shop-list-view-small/", views.shop_list_view_small, name="shop_list_view_small"),
    path("shop-list-view/", views.shop_list_view, name="shop_list_view"),
    path("shop-right-sidebar/", views.shop_right_sidebar, name="shop_right_sidebar"),
    path("shop/", views.shop, name="shop"),
    path("single-product-extended/", views.single_product_extended, name="single_product_extended"),
    path("single-product-fullwidth/", views.single_product_fullwidth, name="single_product_fullwidth"),
    path("single-product-sidebar/", views.single_product_sidebar, name="single_product_sidebar"),
    path("track-your-order/", views.track_your_order, name="track_your_order"),
    path("wishlist/", views.wishlist, name="wishlist"),
]
