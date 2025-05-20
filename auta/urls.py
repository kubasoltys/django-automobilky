from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobilky/', views.AutomobilkyList.as_view(), name='automobilky_list'),
    path('automobilky/<int:pk>/', views.AutomobilkyDetail.as_view(), name='automobilky_detail'),
    path('automobilky/add', views.AutomobilkyCreate.as_view(), name='automobilky_create'),
    path('automobilky/update/<int:pk>', views.AutomobilkyUpdate.as_view(), name='automobilky_update'),
    path('automobilky/delete/<int:pk>', views.AutomobilkyDelete.as_view(), name='automobilky_delete'),
    path('zakladatele/', views.ZakladateleList.as_view(), name='zakladatele_list'),
    path('zakladatele/<int:pk>/', views.ZakladateleDetail.as_view(), name='zakladatele_detail'),
    path('zakladatele/add/', views.ZakladateleCreate.as_view(), name='zakladatele_create'),
    path('zakladatele/update/<int:pk>', views.ZakladateleUpdate.as_view(), name='zakladatele_update'),
    path('zakldatele/delete/<int:pk>', views.ZakladateleDelete.as_view(), name='zakladatele_delete'),
    path('druhy/', views.DruhyList.as_view(), name='druhy_list'),
    path('druhy/<int:pk>/', views.DruhyDetail.as_view(), name='druhy_detail'),
    path('druhy/add', views.DruhyCreate.as_view(), name='druhy_create'),
    path('druhy/update/<int:pk>', views.DruhyUpdate.as_view(), name='druhy_update'),
    path('druhy/delete/<int:pk>', views.DruhyDelete.as_view(), name='druhy_delete'),
]