from django import forms
from .models import Image


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100, label="your name")


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = Image
        fields = ["caption", "image"]
