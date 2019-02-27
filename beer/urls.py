from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fermentable_list_view, name='index'),
]

urlpatterns += (
    # urls for fermentable management
    path('beer/fermentable/', views.fermentable_list_view, name='inventory_fermentable_list'),
    path('beer/fermentable/create/', views.FermentableCreateView.as_view(), name='inventory_fermentable_create'),
    path('beer/fermentable/detail/<int:pk>/', views.FermentableDetailView.as_view(), name='inventory_fermentable_detail'),
    path('beer/fermentable/update/<int:pk>/', views.FermentableUpdateView.as_view(), name='inventory_fermentable_update'),
)
