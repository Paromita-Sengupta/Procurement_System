from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from procurement.models import Supplier, Component


class ComponentAdminForm(forms.ModelForm):
    suppliers = forms.ModelMultipleChoiceField(
        queryset=Supplier.objects.filter(is_authorized=True),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Suppliers',
            is_stacked=False
        )

    )

    class Meta:
        model = Component
        fields = ['name', 'sku', 'suppliers']