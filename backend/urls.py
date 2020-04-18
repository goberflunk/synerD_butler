from django.urls import path

from . import views

app_name = 'backend'

urlpatterns = [
    path('test/',views'
]

urlpatterns = [
    path('testSequence/', views.testSequenceListView.as_view(), name='testSequence_list'),
    path('testSequence/<pk>/', views.SubjectDetailView.as_view(), name='testSequence_detail'),
    path('product/', views.productListView.as_view(), name='product_list'),
    path('product/<pk>/', views.productDetailView.as_view(), name='product_detail'),
    path('performancedata/', views.performancedataListView.as_view(), name='performancedata_list'),
    path('performancedata/<pk>/', views.performancedataDetailView.as_view(), name='performancedata_detail'),
    path('testStandard/', views.testStandardListView.as_view(), name='testStandard_list'),
    path('testStandard/<pk>/', views.testStandardDetailView.as_view(), name='testStandard_detail'),
    path('service/', views.serviceListView.as_view(), name='service_list'),
    path('service/<pk>/', views.serviceDetailView.as_view(), name='service_detail'),
    path('client/', views.clientListView.as_view(), name='client_list'),
    path('client/<pk>/', views.clientDetailView.as_view(), name='client_detail'),
    path('location/', views.locationListView.as_view(), name='location_list'),
    path('location/<pk>/', views.locationDetailView.as_view(), name='location_detail'),
    path('user/', views.userListView.as_view(), name='user_list'),
    path('user/<pk>/', views.userDetailView.as_view(), name='user_detail'),
    path('certificate/', views.certificateListView.as_view(), name='certificate_list'),
    path('certificate/<pk>/', views.certificateDetailView.as_view(), name='certificate_detail')
]
