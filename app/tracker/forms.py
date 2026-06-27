from django import forms
from .models import Student, SessionLog

class SessionLogForm(forms.ModelForm):
    class Meta:
        model = SessionLog
        fields = "__all__"
