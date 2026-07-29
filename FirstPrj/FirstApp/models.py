from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities"
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city


class Address(models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="addresses")
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.address}, {self.district}"


class Customer(models.Model):
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, related_name="customers"
    )
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# models.py の末尾に追加
class WorkoutLog(models.Model):
    exercise = models.CharField(max_length=100)
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise} - {self.weight}kg"
