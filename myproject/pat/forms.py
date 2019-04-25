"""
My forms
"""
from bootstrap_datepicker_plus import DatePickerInput
from django.views import generic
from django import forms


class DateDisplayForm(forms.Form):
    begindate = forms.DateField(widget=DatePickerInput())
    enddate = forms.DateField(widget=DatePickerInput())
