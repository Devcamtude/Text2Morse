from django import forms

class MorseCodeForm(forms.Form):
    text = forms.CharField(label='Enter text', max_length=100)
