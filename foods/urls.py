from django.urls import path

from . import views

app_name = 'foodstuff'
urlpatterns = [

    path(r'', views.IndexView.as_view(), name='index'),

    path('detail', views.DetailView.as_view()),

    path('add_item', views.AddFoodItem.as_view()),

    path(r'<int:pk>/result/', views.ResultsView.as_view(), name='result'),

    path(r'<food_id>/update_quantity/', views.update_quantity, name='update_quantity'),
]
