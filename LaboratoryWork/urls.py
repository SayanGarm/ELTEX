from django.urls import path

from .views import ArticleCreate, ArticleList, ArticleView, ArticleUpdate, ArticleDelete, LabWork

urlpatterns = [
    path('create/', ArticleCreate.as_view(), name='create_article'),
    path('delete/<int:pk>', ArticleDelete.as_view(), name='delete_article'),
    path('update/<int:pk>', ArticleUpdate.as_view(), name='update_article'),
    path('all/', ArticleList.as_view() , name='archive'),
    path('<int:pk>', ArticleView.as_view() , name='article_info'),
    path('laboratory_work/', LabWork.as_view() , name='lab_work')
]