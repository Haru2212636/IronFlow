from django.contrib import admin
from .models import Country, City, Address, Customer

# 作成した4つのモデルを管理画面に表示させるための登録処理
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Customer)
