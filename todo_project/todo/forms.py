from django import forms
import uuid
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()