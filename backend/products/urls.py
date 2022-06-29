from django.urls import path

from . import views

urlpatterns = [
    #int:pk ---> id query ---> api/producs/1  (id=1)
    #localhost:8000/api/products/<int:pk> (id)
    path('', views.product_list_view),
    path('<int:pk>/', views.product_detail_view), 
    path('create/', views.product_create_view), 
    path('<int:pk>/update/', views.product_update_view), 
    path('<int:pk>/delete/', views.product_delete_view), 
]