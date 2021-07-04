from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('area-list/', views.ShowAll, name='area-list'),
    path('area1-detail/<int:pk>/', views.ViewArea1, name='area-detail1'),
    path('area2-detail/<int:pk>/', views.ViewArea2, name='area-detail2'),
    path('area-create1/', views.CreateArea1, name='area1-create'),
    path('area-create2/', views.CreateArea2, name='area2-create'),
    path('area-update1/<int:pk>', views.UpdateArea1, name='area1-update'),
    path('area-update2/<int:pk>', views.UpdateArea2, name='area2-update'),
    path('area-delete1/<int:pk>', views.DeleteArea1, name='area1-delete'),
    path('area-delete2/<int:pk>', views.DeleteArea2, name='area2-delete'),
    

]