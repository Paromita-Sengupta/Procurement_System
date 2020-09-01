from django import forms
from procurement.models import Component, Representatives


class ComponentSearchForm(forms.Form):
    component = forms.ModelChoiceField(
        queryset=Component.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ComponentSearchForm, self).__init__(*args, **kwargs)
        self.fields['component'].widget.attrs.update({"class": "form-control"})

