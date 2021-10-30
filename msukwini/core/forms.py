from django import forms

from msukwini.core.models import Feedback


class CreateFeedbackForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=300,
        label="Email address",
        widget=forms.TextInput(
            attrs={
                "placeholder": "What is your email address?",
                "autocomplete": "off",
                "autocapitalize": "off",
            }
        ),
    )
    name = forms.CharField(
        max_length=1000,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "autocomplete": "off",
                "autocapitalize": "off",
            }
        ),
    )

    class Meta:
        model = Feedback
        fields = (
            "email",
            "name",
            "content",
        )
