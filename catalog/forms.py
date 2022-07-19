from django import forms
from django.forms import RadioSelect

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating", "review")
        widgets = {
            "rating": RadioSelect(
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
            ),
            "review": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "content",
                    "placeholder": "Содержание",
                    "name": "description",
                }
            ),
        }
