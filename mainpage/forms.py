from django.core.mail import send_mail, get_connection

from django.forms.widgets import TextInput

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='sr-only', widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'class': 'form-control', 'id': 'c_name'}))

    email = forms.EmailField(label='sr-only', widget=forms.TextInput(
        attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id': 'c_email'}),
                             required=False)

    message = forms.CharField(label='sr-only', widget=forms.TextInput(
        attrs={'placeholder': 'Message', 'class': 'form-control', 'id': 'c_message'}))


class TreeSplittingForm(forms.Form):
    users = forms.IntegerField(label="Users", max_value=10, min_value=2, widget=forms.NumberInput(
        attrs={'placeholder': 'Users', 'class': 'form-control', 'id': 'c_users'}))

    split = forms.IntegerField(label="Split", max_value=5, min_value=2, widget=forms.NumberInput(
        attrs={'placeholder': 'Split', 'class': 'form-control', 'id': 'c_split'}))

    biased_split = forms.BooleanField(label="Biased Split", initial=False, required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Biased Split', 'class': 'form-control', 'id': 'c_biased_split'}))

    branch_prob = forms.FloatField(label="Branch Prob", min_value=0.1, max_value=0.9, required=False, widget=forms.NumberInput(
        attrs={'placeholder': 'Branch Prob', 'class': 'form-control', 'id': 'c_branch_prob'}))

    k = forms.IntegerField(label="K", min_value=1, max_value=5, widget=forms.NumberInput(
        attrs={'placeholder': 'K', 'class': 'form-control', 'id': 'c_k'}))

    modified = forms.BooleanField(label="Modified", initial=False, required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Modified', 'class': 'form-control', 'id': 'c_modified'}))

    unisplit = forms.BooleanField(label="Unisplit", initial=False, required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Unisplit', 'class': 'form-control',  'id': 'c_unisplit'}))

    sic = forms.BooleanField(label="SIC", initial=False, required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'SIC', 'class': 'form-control', 'id': 'c_sic'}))

