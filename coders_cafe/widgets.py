from django import forms


class DatePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'
