from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cosmic_news/', views.show_cosmic_news, name='cosmic_news'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('show-csv/', views.show_csv, name='show_csv'),
]