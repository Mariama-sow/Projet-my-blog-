from django.urls import path 

from .views import home , ArticlesCreateView , ArticlesDeleteView , ArticlesUpdateView , ArticlesListView , ArticlesDetailView , add_comment

urlpatterns = [
    path('detail/<int:pk>/',ArticlesDetailView.as_view(), name='detail_article' ),
    path('update/<int:pk>/',ArticlesUpdateView.as_view(), name='update_article' ),
    path('delete/<int:pk>/',ArticlesDeleteView.as_view(), name='delete_article' ),
    path('form/',ArticlesCreateView.as_view(), name='formulaire' ),
    path('',ArticlesListView.as_view() ,name='List_articles'),
    path('add-comment/<int:id>/', add_comment, name='add-comment'),
] 