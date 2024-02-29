from django.urls import path
from userauths import views

app_name="userauths"

urlpatterns = [
    path("sign-up/", views.register_view,name="sign-up"),
    path("sign-in/", views.login_view,name="sign-in"),
    path("sign-out/", views.logout_view,name="sign-out"),
    path("shop/", views.shop_view,name="shop"),
    path("blog/",views.blog_view,name="blog"),
    path("about/", views.about_view,name="about"),
    path("contact/", views.contact_view,name="contact"),
]
