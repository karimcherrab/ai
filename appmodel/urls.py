from django.urls import path
from .views import knn_Dropped , knn_Frequent,kmeans_Dropped,kmeans_Frequent

urlpatterns = [
    path('knn_Dropped/', knn_Dropped, name='knn_Dropped'),
    path('knn_Frequent/', knn_Frequent, name='knn_Frequent'),

    
    
    path('kmeans_Dropped/', kmeans_Dropped, name='kmeans_Dropped'),
    path('kmeans_Frequent/', kmeans_Frequent, name='kmeans_Frequent'),

]