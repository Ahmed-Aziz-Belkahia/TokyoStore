from django.shortcuts import render

# Create your views here.

def cart(request, *args, **kwargs):
    return render(request, "shop/cart.html", {})

def checkout(request, *args, **kwargs):
    return render(request, "shop/checkout.html", {})

def compare(request, *args, **kwargs):
    return render(request, "shop/compare.html", {})

def my_account(request, *args, **kwargs):
    return render(request, "shop/my-account.html", {})

def product_categories_4_column_sidebar(request, *args, **kwargs):
    return render(request, "shop/product-categories-4-column-sidebar.html", {})

def product_categories_5_column_sidebar(request, *args, **kwargs):
    return render(request, "shop/product-categories-5-column-sidebar.html", {})

def product_categories_6_column_full_width(request, *args, **kwargs):
    return render(request, "shop/product-categories-6-column-full-width.html", {})

def product_categories_7_column_full_width(request, *args, **kwargs):
    return render(request, "shop/product-categories-7-column-full-width.html", {})

def shop_3_columns_sidebar(request, *args, **kwargs):
    return render(request, "shop/shop-3-columns-sidebar.html", {})

def shop_4_columns_sidebar(request, *args, **kwargs):
    return render(request, "shop/shop-4-columns-sidebar.html", {})

def shop_5_columns_sidebar(request, *args, **kwargs):
    return render(request, "shop/shop-5-columns-sidebar.html", {})

def shop_6_columns_full_width(request, *args, **kwargs):
    return render(request, "shop/shop-6-columns-full-width.html", {})

def shop_7_columns_full_width(request, *args, **kwargs):
    return render(request, "shop/shop-7-columns-full-width.html", {})

def shop_full_width(request, *args, **kwargs):
    return render(request, "shop/shop-full-width.html", {})

def shop_grid_extended(request, *args, **kwargs):
    return render(request, "shop/shop-grid-extended.html", {})

def shop_grid(request, *args, **kwargs):
    return render(request, "shop/shop-grid.html", {})

def shop_left_sidebar(request, *args, **kwargs):
    return render(request, "shop/shop-left-sidebar.html", {})

def shop_list_view_small(request, *args, **kwargs):
    return render(request, "shop/shop-list-view-small.html", {})

def shop_list_view(request, *args, **kwargs):
    return render(request, "shop/shop-list-view.html", {})

def shop_right_sidebar(request, *args, **kwargs):
    return render(request, "shop/shop-right-sidebar.html", {})

def shop(request, *args, **kwargs):
    return render(request, "shop/shop.html", {})

def single_product_extended(request, *args, **kwargs):
    return render(request, "shop/single-product-extended.html", {})

def single_product_fullwidth(request, *args, **kwargs):
    return render(request, "shop/single-product-fullwidth.html", {})

def single_product_sidebar(request, *args, **kwargs):
    return render(request, "shop/single-product-sidebar.html", {})

def track_your_order(request, *args, **kwargs):
    return render(request, "shop/track-your-order.html", {})

def wishlist(request, *args, **kwargs):
    return render(request, "shop/wishlist.html", {})