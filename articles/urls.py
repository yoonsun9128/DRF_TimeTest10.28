from django.urls import path, include
from articles import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticlesView.as_view(), name="Articlesview"),
]