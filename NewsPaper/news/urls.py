from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetail, NewsSearch, NewsCreate, NewsDelete, NewsUpdate

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', NewsSearch.as_view(), name='post_search'),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='post_update'),
    path('article/create/', NewsCreate.as_view()),
]
