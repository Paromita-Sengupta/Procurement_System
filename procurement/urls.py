from django.urls import path
from procurement.views import ComponentSearchView, DocumentationView
from procurement.api import ComponentAPIList, ComponentAPIRetrieve

urlpatterns = [
    path('', ComponentSearchView.as_view(), name='component-search'),
    path('documentation', DocumentationView.as_view(), name='documentation'),

    # API Urls
    path('api/components/', ComponentAPIList.as_view(), name='api-component-list'),
    path('api/components/<int:pk>/', ComponentAPIRetrieve.as_view(), name='api-component-retrieve'),
]
