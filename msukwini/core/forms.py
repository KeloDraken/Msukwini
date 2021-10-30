from django import forms

from msukwini.core.models import Feedback


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            "email",
            "name",
            "content",
        )
