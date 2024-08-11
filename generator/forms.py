from django import forms

class TextInputForm(forms.Form):
    text_input = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter text to generate an image'})
    )