from django import forms


class CheckInForm(forms. Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=225)
    contact_number = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    guest_number = forms.IntegerField(max_value=6)
    checkIns = forms.CharField(max_length=50)
    checkOut = forms.CharField(max_length=50)
    code = forms.CharField(max_length=6)
