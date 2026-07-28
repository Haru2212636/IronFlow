from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-log", views.add_log, name="add_log"),  # ← この行を追加（HTMX用URL）
]
