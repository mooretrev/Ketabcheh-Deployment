from django.urls import path

from . import views

app_name = 'keta'
urlpatterns = [
    path('', views.index, name='index'),
    # path('name/', views.get_name, name='get_name'),
    # path('display_name/', views.display_name, name='display_name'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
