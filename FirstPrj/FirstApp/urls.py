from django.urls import path
from . import views

urlpatterns = [
    # 既存のpathがあれば残しておきます
    path("add/", views.add_customer, name="add-customer"),
    path("search/", views.search_customers, name="search-customers"),
]
