from django.contrib import admin
from django.urls import path
from FirstApp import views  # [cite: 1]

urlpatterns = [
    path("admin/", admin.site.urls),  # [cite: 1]
    path("hello", views.hello),  # スライドにあったものでも可[cite: 1]
    path("", views.index, name="view-index"),  # [cite: 1]
    path("cars/", views.list_cars, name="list-cars"),
    path("form/", views.show_form, name="show-form"),
    path("process/", views.process_request, name="process-request"),
    path("redirect/", views.redirect_home, name="redirect-home"),
]
