"""Forms for FirstApp customer application."""

from django import forms


class CustomerForm(forms.Form):
    """新規顧客登録用フォーム (POST用)"""

    first_name = forms.CharField(label="First Name", max_length=45)
    last_name = forms.CharField(label="Last Name", max_length=45)
    email = forms.EmailField(label="Email Address", required=False)
    address_id = forms.IntegerField(label="Address ID")
    store_id = forms.IntegerField(label="Store ID", initial=1)


class CustomerSearchForm(forms.Form):
    """顧客検索用フォーム (GET用)"""

    search_query = forms.CharField(
        label="Search Customer Name", max_length=45, required=False
    )
