from django.contrib import admin
from django.shortcuts import render_to_response, get_object_or_404
from procurement.admin_forms import ComponentAdminForm
from procurement.models import Supplier, Component, Representatives



class RepresentativeAdmin(admin.ModelAdmin):

    list_display = ('representative_name','representative_email', "phone_number")
    list_filter = ('representative_name', )
    readonly_fields = ['representative_name','representative_email', "phone_number"]

    # To give access only to the user admin to maintain the data, others can only read/view the data
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields


class SupplierAdmin(admin.ModelAdmin):

    filter_horizontal = ('representatives','components')
    fields = ['name','representatives',"is_authorized"]
    readonly_fields = ['representatives', ]
    list_display = ('name',  'get_repname' , 'get_repemail','get_repcontact','is_authorized','updated')
    ordering =  ('name',)
    list_filter = ('name','is_authorized')

    # To give access only to the user admin to maintain the data
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []

        return self.readonly_fields



class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'updated')
    form = ComponentAdminForm
    source_components_template = 'procurement/admin_templates/source_components.html'

    def source_components(self, request, pk):
        component = get_object_or_404(Component, pk=pk)

        return render_to_response(self.source_components_template, {
            'title': 'Source Suppliers for: %s' % component,
            'opts': self.model._meta,
            'component': component,
            'supplier_results': component.suppliers.filter(is_authorized=True)

        })

# Representative Model is registered
admin.site.register(Representatives,RepresentativeAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Component, ComponentAdmin)
