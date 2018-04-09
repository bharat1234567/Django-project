from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    # ex: /polls/
    path('top-five/', views.showtopfivealter, name='top-five'),
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name="welcome"),
    path('<int:question_id>/', views.detail2, name='detailed'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='resulted'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='voted'),
]
