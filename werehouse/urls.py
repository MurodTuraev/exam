from django.urls import path
from werehouse import views

urlpatterns = [
    path('categories/', views.CategoryAPIView.as_view(), name='category-list'),
    path('materials/', views.RawMaterialAPIView.as_view(), name='material-list'),
    path('product-materials/', views.CategoryRawMaterialAPIView.as_view(), name='product-materials-list'),
    path('warehouse/', views.WarehouseAPIView.as_view(), name='warehouses-list'),
    path('material-needed/', views.RawMaterialsNeeded.as_view(), name='material-needed'),
]